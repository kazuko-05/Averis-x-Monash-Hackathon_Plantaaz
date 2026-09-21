"""
End-to-End Shipping Document Verification Pipeline.

Orchestrates the entire verification flow:
Email Inbox -> Classification -> Reliability Triage -> Extraction -> Comparison -> Reporting.
"""

import json
from pathlib import Path
from typing import Dict, Any, List, Tuple, Optional

from src.classifier import EmailClassifier
from src.reliability import ReliabilityGate
from src.extractor import DocumentExtractor
from src.comparator import ShipmentComparator


class VerificationPipeline:
    """Complete verification pipeline for processing shipping operations emails."""

    def __init__(self, data_root: str = "data_v2"):
        self.data_root = Path(data_root)
        self.classifier = EmailClassifier()
        self.reliability = ReliabilityGate(data_root=str(self.data_root))
        self.extractor = DocumentExtractor(data_root=str(self.data_root))
        self.comparator = ShipmentComparator()

    def process_email(self, email_record: Dict[str, Any]) -> Dict[str, Any]:
        """
        Processes a single email record through the complete verification pipeline.

        Returns an enriched dict containing both the submission-standard fields:
        {category, status, review_reason, defect_fields, has_defect, decided_by}
        plus operational report context: {summary, discrepancies, extracted_si, extracted_bl}.
        """
        eid = email_record.get("email_id", "unknown")
        cat, decided_by = self.classifier.classify(email_record)

        result: Dict[str, Any] = {
            "email_id": eid,
            "subject": email_record.get("subject", ""),
            "from": email_record.get("from", ""),
            "category": cat,
            "status": "OK",
            "review_reason": None,
            "defect_fields": [],
            "has_defect": False,
            "decided_by": decided_by,
            "summary": "Email categorized successfully.",
            "discrepancies": [],
            "extracted_si": {},
            "extracted_bl": {},
            "escalation_details": {},
        }

        if cat != "BL_COMPARISON":
            return result

        # Reliability Check (Human-in-the-loop gate)
        needs_review, reason, details = self.reliability.evaluate(email_record)
        if needs_review:
            result["status"] = "NEEDS_REVIEW"
            result["review_reason"] = reason
            result["escalation_details"] = details
            result["summary"] = f"Escalated for human review: {reason} ({details.get('reason_explanation', '')})"
            return result

        attachments = email_record.get("attachments", [])
        if len(attachments) == 2:
            si_list = [a for a in attachments if "_SI." in a]
            bl_list = [a for a in attachments if "_BL." in a]
            si_path = si_list[0] if si_list else attachments[0]
            bl_path = bl_list[0] if bl_list else attachments[1]

            si_data = self.extractor.extract(si_path)
            bl_data = self.extractor.extract(bl_path)
            comp_res = self.comparator.compare(si_data, bl_data)

            result["status"] = comp_res["status"]
            result["has_defect"] = comp_res["has_defect"]
            result["defect_fields"] = comp_res["defect_fields"]
            result["discrepancies"] = comp_res["discrepancies"]
            result["summary"] = comp_res["summary"]
            result["extracted_si"] = si_data
            result["extracted_bl"] = bl_data
        elif len(attachments) == 0:
            result["summary"] = "BL comparison request received; awaiting draft BL from carrier/customer."
        else:
            result["summary"] = f"Received {len(attachments)} attachments."

        return result

    def process_inbox(self) -> Tuple[Dict[str, Any], List[Dict[str, Any]]]:
        """
        Runs the verification pipeline over every email in the inbox directory.

        Returns:
            Tuple of:
            - submission: Dict keyed by email_id for benchmark evaluation
            - detailed_records: List of enriched result dictionaries
        """
        inbox_dir = self.data_root / "inbox"
        email_files = sorted(inbox_dir.glob("email_*.json"))

        submission: Dict[str, Any] = {}
        detailed_records: List[Dict[str, Any]] = []

        for p in email_files:
            with open(p, "r", encoding="utf-8") as f:
                record = json.load(f)

            res = self.process_email(record)
            detailed_records.append(res)

            submission[res["email_id"]] = {
                "category": res["category"],
                "status": res["status"],
                "review_reason": res["review_reason"],
                "defect_fields": res["defect_fields"],
                "has_defect": res["has_defect"],
                "decided_by": res["decided_by"],
            }

        return submission, detailed_records

    def save_submission(self, submission: Dict[str, Any], output_path: str = "submission.json") -> Path:
        """Saves the submission dictionary to a JSON file."""
        out = Path(output_path)
        with open(out, "w", encoding="utf-8") as f:
            json.dump(submission, f, indent=2, ensure_ascii=False)
        return out

    def generate_discrepancy_report(
        self, detailed_records: List[Dict[str, Any]], output_path: str = "discrepancy_report.md"
    ) -> Path:
        """Generates a human-readable operational discrepancy report."""
        out = Path(output_path)

        total = len(detailed_records)
        cat_counts: Dict[str, int] = {}
        mismatches = [r for r in detailed_records if r["status"] == "MISMATCH"]
        needs_review = [r for r in detailed_records if r["status"] == "NEEDS_REVIEW"]
        clean_docs = [r for r in detailed_records if r["category"] == "BL_COMPARISON" and r["status"] == "OK"]

        for r in detailed_records:
            cat_counts[r["category"]] = cat_counts.get(r["category"], 0) + 1

        lines = [
            "# Shipping Document Verification - Discrepancy & Operational Report",
            "",
            "## Executive Summary",
            f"- **Total Emails Ingested**: {total}",
            f"- **BL Document Checks**: {cat_counts.get('BL_COMPARISON', 0)}",
            f"  - **Discrepancies Caught (MISMATCH)**: {len(mismatches)}",
            f"  - **Clean Matches (OK)**: {len(clean_docs)}",
            f"  - **Escalated to Human Review (NEEDS_REVIEW)**: {len(needs_review)}",
            f"- **SI Requests**: {cat_counts.get('SI_REQUEST', 0)}",
            f"- **Invoice Queries**: {cat_counts.get('INVOICE_QUERY', 0)}",
            f"- **General Updates**: {cat_counts.get('GENERAL', 0)}",
            f"- **Spam Filtered**: {cat_counts.get('SPAM', 0)}",
            "",
            "---",
            "",
            "## Document Comparison Discrepancies (Immediate Attention Required)",
            "",
            "| Email ID | Subject | Mismatched Fields | Side-by-Side Values (SI vs BL) |",
            "|---|---|---|---|",
        ]

        for r in mismatches:
            diffs = "<br>".join([f"**{d['field']}**: {d['display']}" for d in r["discrepancies"]])
            fields_str = ", ".join(r["defect_fields"])
            lines.append(f"| `{r['email_id']}` | {r['subject']} | {fields_str} | {diffs} |")

        lines.extend([
            "",
            "---",
            "",
            "## Human Review Queue (Escalated Cases)",
            "",
            "| Email ID | Escalation Reason | Evidence / Context | Recommended Operator Action |",
            "|---|---|---|---|",
        ])

        for r in needs_review:
            reason = r["review_reason"]
            explanation = r["escalation_details"].get("reason_explanation", "Manual review required.")
            if reason == "wrong_doc_type":
                action = "Request draft Bill of Lading from customer/agent; current attachment is non-BL."
            elif reason == "missing_attachment":
                action = "Contact sender to re-attach dropped draft BL or verify thread attachments."
            elif reason == "unreadable":
                action = "Route to OCR engine or request higher resolution non-corrupt document."
            elif reason == "missing_value":
                action = "Contact shipper/customer to populate blank mandatory fields before re-check."
            else:
                action = "Review case manually."

            lines.append(f"| `{r['email_id']}` | `{reason}` | {explanation} | {action} |")

        lines.extend([
            "",
            "---",
            "",
            "*Report generated autonomously by SDOC Verification Pipeline.*",
        ])

        with open(out, "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")

        return out
