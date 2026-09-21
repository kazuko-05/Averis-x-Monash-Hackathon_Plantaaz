"""
Automated Verification & Regression Test Suite.

Validates:
1. Email classification accuracy across all 5 categories.
2. Multi-format attachment extraction (TXT, PDF, DOCX, XLSX).
3. Reliability gate and human review escalation on all edge cases with 0 false alarms.
4. Side-by-side discrepancy comparator against gold truth defects.
5. Official benchmark scoring achieving 1.0 (100%).
"""

import json
import unittest
from pathlib import Path

from src.classifier import EmailClassifier
from src.reliability import ReliabilityGate
from src.extractor import DocumentExtractor
from src.comparator import ShipmentComparator
from src.pipeline import VerificationPipeline
from server import scoring

WORKSPACE_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = WORKSPACE_ROOT / "data_v2"
GT_PATH = DATA_DIR / "ground_truth.json"


class TestShippingDocumentVerification(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        with open(GT_PATH, "r", encoding="utf-8") as f:
            cls.ground_truth = json.load(f)

    def test_01_classification_accuracy(self):
        """Test that EmailClassifier achieves 100% accuracy on all 520 inbox emails."""
        classifier = EmailClassifier()
        correct = 0
        total = len(self.ground_truth)

        for eid, truth in self.ground_truth.items():
            email_path = DATA_DIR / "inbox" / f"{eid}.json"
            with open(email_path, "r", encoding="utf-8") as f:
                email_rec = json.load(f)

            pred_cat, decided_by = classifier.classify(email_rec)
            self.assertEqual(decided_by, "rule")
            if pred_cat == truth["category"]:
                correct += 1

        acc = correct / total
        self.assertEqual(acc, 1.0, f"Expected 100% accuracy, got {acc:.4f} ({correct}/{total})")

    def test_02_reliability_escalation(self):
        """Test that ReliabilityGate correctly escalates all 20 edge cases with 0 false alarms."""
        gate = ReliabilityGate(data_root=str(DATA_DIR))

        # Check the 20 edge cases (email_501 to email_520)
        for i in range(501, 521):
            eid = f"email_{i:03d}"
            truth = self.ground_truth[eid]
            email_path = DATA_DIR / "inbox" / f"{eid}.json"
            with open(email_path, "r", encoding="utf-8") as f:
                email_rec = json.load(f)

            needs_review, reason, details = gate.evaluate(email_rec)
            self.assertTrue(needs_review, f"{eid} should need review")
            self.assertEqual(
                reason, truth["review_reason"],
                f"{eid} expected review reason '{truth['review_reason']}', got '{reason}'"
            )

        # Check that 1-500 produce 0 false alarms
        for i in range(1, 501):
            eid = f"email_{i:03d}"
            truth = self.ground_truth[eid]
            if truth["category"] == "BL_COMPARISON":
                email_path = DATA_DIR / "inbox" / f"{eid}.json"
                with open(email_path, "r", encoding="utf-8") as f:
                    email_rec = json.load(f)

                needs_review, reason, _ = gate.evaluate(email_rec)
                self.assertFalse(needs_review, f"{eid} was falsely escalated for review: {reason}")

    def test_03_multi_format_extraction_and_comparison(self):
        """Test extraction across TXT, PDF, DOCX, XLSX and exact defect field detection."""
        extractor = DocumentExtractor(data_root=str(DATA_DIR))
        comparator = ShipmentComparator()

        tested_pairs = 0
        exact_matches = 0

        for i in range(1, 501):
            eid = f"email_{i:03d}"
            truth = self.ground_truth[eid]
            if truth["category"] != "BL_COMPARISON":
                continue

            email_path = DATA_DIR / "inbox" / f"{eid}.json"
            with open(email_path, "r", encoding="utf-8") as f:
                email_rec = json.load(f)

            attachments = email_rec.get("attachments", [])
            if len(attachments) != 2:
                continue

            tested_pairs += 1
            si_path = [a for a in attachments if "_SI." in a][0]
            bl_path = [a for a in attachments if "_BL." in a][0]

            si_data = extractor.extract(si_path)
            bl_data = extractor.extract(bl_path)
            comp_res = comparator.compare(si_data, bl_data)

            pred_defects = set(comp_res["defect_fields"])
            gold_defects = set(truth["defect_fields"])

            self.assertEqual(
                pred_defects, gold_defects,
                f"Mismatch in defect detection for {eid}: Pred {pred_defects} != Gold {gold_defects}"
            )
            exact_matches += 1

        self.assertEqual(exact_matches, tested_pairs)
        self.assertEqual(tested_pairs, 109)

    def test_04_end_to_end_pipeline_and_benchmark(self):
        """Test complete pipeline execution and benchmark scoring achieving 1.0 (100%)."""
        pipeline = VerificationPipeline(data_root=str(DATA_DIR))
        submission, records = pipeline.process_inbox()

        self.assertEqual(len(records), 520)
        self.assertEqual(len(submission), 520)

        scoreboard = scoring.score_all(self.ground_truth, submission)

        self.assertEqual(scoreboard["stage1"]["macro_f1"], 1.0)
        self.assertEqual(scoreboard["stage1"]["accuracy"], 1.0)
        self.assertEqual(scoreboard["stage3"]["defect_f1"], 1.0)
        self.assertEqual(scoreboard["stage3"]["exact_match_rate"], 1.0)
        self.assertEqual(scoreboard["reliability"]["escalation_recall"], 1.0)
        self.assertEqual(scoreboard["reliability"]["escalation_precision"], 1.0)
        self.assertEqual(scoreboard["end_to_end"]["rate"], 1.0)
        self.assertEqual(scoreboard["end_to_end"]["success"], 46)
        self.assertEqual(scoreboard["final_score"], 1.0)


if __name__ == "__main__":
    unittest.main()
