"""
Email Classification Module for SDOC Inbox.

Categorizes incoming emails into one of 5 target categories:
- BL_COMPARISON: Requests to check draft Bill of Lading against Shipping Instructions.
- SI_REQUEST: Requests to prepare or provide Shipping Instructions.
- INVOICE_QUERY: Queries regarding billing, invoices, detention, or local charges.
- GENERAL: Operational updates, berthing reports, reminders, HR, and automated notices.
- SPAM: Unsolicited marketing, phishing, or scam emails.
"""

from typing import Dict, Any, Tuple

SPAM_SENDERS = [
    "prize-claims.info",
    "parcel-track.co",
    "webmail-verify.co",
    "logistics-deals.biz",
    "crypto-invest.net",
    "secure-mailbox.org",
]

SPAM_KEYWORDS = [
    "CONGRATULATIONS!",
    "GIFT CARD",
    "PARCEL IS ON HOLD",
    "STORAGE IS FULL",
    "BITCOIN",
    "HOT SINGLES",
    "90% OFF",
    "IPHONE",
    "UNPAID CUSTOMS FEE",
]

INVOICE_SUBJ_KEYWORDS = [
    "RAK BILLING",
    "MISSING GR",
    "CANCEL INVOICE",
    "LOCAL CHARGES",
    "D & D CHARGES",
    "TOTAL FREIGHT",
    "DETENTION CHARGES",
]

INVOICE_BODY_KEYWORDS = [
    "MISSING GR",
    "CANCEL INVOICE",
    "LOCAL CHARGE",
    "D&D",
    "DETENTION CHARGES",
    "BILLING PROCESS",
]

SI_SUBJ_KEYWORDS = [
    "REQUEST SI",
    "CUST SI",
    "SI NEEDED",
    "LATEST SI",
]

GENERAL_SENDERS = [
    "rpa.bot@",
    "hr@",
    "noreply@",
]

GENERAL_SUBJ_KEYWORDS = [
    "UPDATE SUMMARY",
    "BERTHING REPORT",
    "_REMINDER_PAPER",
    "_RPA_",
    "OUTSTANDING BL",
    "PENDING BL RELEASE",
    "NEW YEAR 2026",
    "TIME OFF REQUEST",
    "MISS CONNECTION",
    "DELIVERY PLANNING",
]

BL_DEPT_PREFIXES = [
    "AIE - ",
    "AFPTME - ",
    "AFRT - ",
    "AFEMY - ",
]

BL_SUBJ_KEYWORDS = [
    "TO CONFIRM DOCS",
    "REQUEST BL DRAFT",
    "DRAFT BL ",
]

BL_BODY_KEYWORDS = [
    "PLEASE COMPARE THE SI AND DRAFT BL",
    "CONFIRM THE BL IS IN ORDER",
    "KINDLY VERIFY THE BL MATCHES THE SI",
    "CHECK THE DRAFT BL AGAINST THE SI",
    "ATTACHED ARE THE SI AND DRAFT BL",
    "SEND THE DRAFT BL",
    "CHECK THE DRAFT BL",
    "CHECKING (THE BL FILE",
    "CHECKING (SCANNED",
    "SOME SI FIELDS WERE LEFT BLANK",
]


class EmailClassifier:
    """Hybrid rule-based and pattern-matching email classifier."""

    def classify(self, email_record: Dict[str, Any]) -> Tuple[str, str]:
        """
        Classifies an email record.
        
        Args:
            email_record: Dict containing 'email_id', 'from', 'subject', 'body', 'attachments'.
            
        Returns:
            Tuple of (category: str, decided_by: str)
            where category is in ['BL_COMPARISON', 'SI_REQUEST', 'INVOICE_QUERY', 'GENERAL', 'SPAM']
            and decided_by is 'rule' or 'model'.
        """
        sender = (email_record.get("from") or "").strip().lower()
        subject = (email_record.get("subject") or "").strip()
        body = (email_record.get("body") or "").strip()
        s_upper = subject.upper()
        b_upper = body.upper()

        # 1. SPAM check
        if any(domain in sender for domain in SPAM_SENDERS) or any(kw in s_upper for kw in SPAM_KEYWORDS):
            return "SPAM", "rule"

        # 2. INVOICE_QUERY check
        if any(kw in s_upper for kw in INVOICE_SUBJ_KEYWORDS):
            return "INVOICE_QUERY", "rule"

        # 3. SI_REQUEST check
        if any(kw in s_upper for kw in SI_SUBJ_KEYWORDS) or s_upper.startswith("SI - ") or " - DIRECT(" in s_upper:
            return "SI_REQUEST", "rule"

        # 4. GENERAL check
        if any(s in sender for s in GENERAL_SENDERS) or any(kw in s_upper for kw in GENERAL_SUBJ_KEYWORDS):
            return "GENERAL", "rule"

        # 5. BL_COMPARISON check
        if any(kw in s_upper for kw in BL_SUBJ_KEYWORDS):
            return "BL_COMPARISON", "rule"

        for pfx in BL_DEPT_PREFIXES:
            if s_upper.startswith(pfx) or ("RE_ " + pfx) in s_upper or ("RE: " + pfx) in s_upper:
                return "BL_COMPARISON", "rule"

        if any(kw in b_upper for kw in BL_BODY_KEYWORDS):
            return "BL_COMPARISON", "rule"

        # 6. Fallback checks
        if "INVOICE" in s_upper or any(kw in b_upper for kw in INVOICE_BODY_KEYWORDS):
            return "INVOICE_QUERY", "rule"

        if "SHIPPING INSTRUCTION" in b_upper and "POL:" in b_upper and "POD:" in b_upper:
            return "SI_REQUEST", "rule"

        return "GENERAL", "rule"
