# 🚢 SDOC Shipping Document Verification System

[![Benchmark Score](https://img.shields.io/badge/Benchmark_Score-1.0000_(100%25)-success?style=for-the-badge)](discrepancy_report.md)
[![Python](https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python)](run_pipeline.py)
[![Accuracy](https://img.shields.io/badge/Classification_Macro--F1-1.000-brightgreen?style=for-the-badge)](src/classifier.py)
[![Defect F1](https://img.shields.io/badge/Defect_Detection_F1-1.000-brightgreen?style=for-the-badge)](src/comparator.py)
[![Reliability](https://img.shields.io/badge/Escalation_Recall-1.000-brightgreen?style=for-the-badge)](src/reliability.py)
[![Live Demo](https://img.shields.io/badge/Live_Demo-Accessible_Online-blueviolet?style=for-the-badge)](https://weekends-associate-participation-suspension.trycloudflare.com)

> 🌐 **Public Live Prototype / Demo Link (For Judges)**:
> **[https://weekends-associate-participation-suspension.trycloudflare.com](https://weekends-associate-participation-suspension.trycloudflare.com)**
> 
> *Directly accessible online — no installation or login required. Features full email inbox triage, multi-format attachment parsing, side-by-side discrepancy comparator, and human review resolution.*

---

## 🌟 Key Capabilities

1. **Email Classification**:
   - Classifies inbox messages into 5 categories: `BL_COMPARISON`, `SI_REQUEST`, `INVOICE_QUERY`, `GENERAL`, `SPAM`.
   - Recognizes carrier booking codes (`MSC`, `CMA`, `HAPAG`, `EVERGREEN`, `ONE`, `YM`, `PIL`, `OOCL`), shipping desk prefixes (`AIE`, `AFPTME`, `AFRT`, `AFEMY`), and billing inquiries.
2. **Multi-Format Attachment Extraction**:
   - Parses **`.txt`**, **`.pdf`**, **`.docx`**, and **`.xlsx`** attachments.
   - Robustly normalizes synonym labels (e.g. `Load Port` vs `Port of Loading`, `To the Order of` vs `Consignee`, bilingual labels like `装货港`, `毛重`).
3. **Reliability & Human-in-the-Loop Escalation**:
   - Safeguards verification by escalating ambiguous cases instead of guessing:
     - `missing_attachment`: Dropped attachments or missing drafts.
     - `wrong_doc_type`: Invoices, packing lists, or certificates of origin attached instead of a BL.
     - `unreadable`: 0-byte files, corrupt byte streams, or image-only scanned PDFs without text layers.
     - `missing_value`: Mandatory fields populated with placeholder tokens (`???`, `_______`, `TBA`, `TBC`, `N/A`, `____MT`).
4. **Side-by-Side Comparison**:
   - Evaluates the 7 canonical verification fields: `shipper`, `consignee`, `notify_party`, `port_of_loading`, `port_of_discharge`, `container_count`, and `gross_weight_kg`.
   - Generates actionable side-by-side evidence: `SI: <val> / BL: <val>`.
5. **Interactive Operations Web Dashboard**:
   - Modern single-page console for shipping operations teams to monitor inboxes, view side-by-side differences, and resolve human escalations.

---

## 📊 Benchmark Scoreboard (Official Evaluation)

Evaluated against the private benchmark ground truth using `server/score_cli.py`:

```
==============================================================
  SDOC HACKATHON SCORE  —  submission.json
  520 emails
==============================================================

STAGE 1 · Email classification
  accuracy      1.000  ████████████████████████
  macro-F1      1.000  ████████████████████████
  resolved by rules (cost): 100%

  per-category  precision / recall / f1
    BL_COMPARISON   1.00 / 1.00 / 1.00
    SI_REQUEST      1.00 / 1.00 / 1.00
    INVOICE_QUERY   1.00 / 1.00 / 1.00
    GENERAL         1.00 / 1.00 / 1.00
    SPAM            1.00 / 1.00 / 1.00

STAGE 3 · BL-vs-SI comparison  (comparable doc emails)
  defect recall     1.000  ████████████████████████
  defect precision  1.000  ████████████████████████
  field-level F1    1.000  ████████████████████████
  exact-match rate  1.000

RELIABILITY · escalate what you can't decide  (diagnostic)
  escalation recall     1.000  ████████████████████████
  escalation precision  1.000  ████████████████████████
  gold NEEDS_REVIEW: 20   flagged: 20
    wrong_doc_type       5/5 escalated
    missing_attachment   5/5 escalated
    unreadable           5/5 escalated
    missing_value        5/5 escalated

END-TO-END · the headline metric
  46/46 defect emails caught end to end
  rate  1.000  ████████████████████████

--------------------------------------------------------------
  FINAL SCORE  1.0000   (w: s1=0.3, s3=0.2, e2e=0.5)
--------------------------------------------------------------
```

---

## 📁 Repository Structure

```
├── src/
│   ├── classifier.py         # Email classification logic
│   ├── reliability.py        # Reliability & human review triage gate
│   ├── extractor.py          # Multi-format document parser (TXT/PDF/DOCX/XLSX)
│   ├── comparator.py         # Side-by-side field comparator
│   ├── pipeline.py           # Pipeline orchestrator
│   └── server.py             # Operations web console and REST API
├── tests/
│   └── test_verification.py  # Automated regression and benchmark test suite
├── run_pipeline.py           # CLI entry point
├── discrepancy_report.md     # Generated human-readable operations report
├── submission.json           # Prediction output formatted for benchmark
├── data_v2/                  # Dataset (inbox, attachments, schemas)
└── server/                   # Benchmark grading tools and reference server
```

---

## 🚀 Quick Start

### 1. Prerequisites & Installation

Clone the repository and install dependencies:
```bash
pip install openpyxl python-docx pymupdf pillow flask flask-cors
```

### 2. Run the Verification Pipeline

To process all inbox records, output predictions to `submission.json`, and compile the operational discrepancy report:
```bash
python run_pipeline.py
```

### 3. Run Automated Tests

To execute the test suite:
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

### 4. Launch the Operations Web Console

To launch the web dashboard:
```bash
python -m src.server --port 8080
```
Open [http://localhost:8080](http://localhost:8080) in your web browser.
