# 🚢 SDOC Verification Platform — Team Plantaaz

> **Averis x Monash University Hackathon 2026**  
> *An Autonomous Shipping Document Verification & Operational Discrepancy Detection System*

[![Benchmark Score](https://img.shields.io/badge/Benchmark_Score-1.0000_(100%25)-success?style=for-the-badge)](discrepancy_report.md)
[![Python](https://img.shields.io/badge/Python-3.14-blue?style=for-the-badge&logo=python)](run_pipeline.py)
[![Classification F1](https://img.shields.io/badge/Classification_Macro--F1-1.000-brightgreen?style=for-the-badge)](src/classifier.py)
[![Defect F1](https://img.shields.io/badge/Defect_Detection_F1-1.000-brightgreen?style=for-the-badge)](src/comparator.py)
[![Reliability](https://img.shields.io/badge/Escalation_Recall-1.000-brightgreen?style=for-the-badge)](src/reliability.py)
[![Live Demo](https://img.shields.io/badge/Live_Demo-Accessible_Online-blueviolet?style=for-the-badge)](https://weekends-associate-participation-suspension.trycloudflare.com)

---

## 🌐 Live Prototype & Submission Links

| Deliverable | Link / Access |
|---|---|
| **Live Working Prototype (Mandatory)** | 🔗 **[https://weekends-associate-participation-suspension.trycloudflare.com](https://weekends-associate-participation-suspension.trycloudflare.com)** |
| **GitHub Repository** | 🔗 **[https://github.com/kazuko-05/Averis-x-Monash-Hackathon_Plantaaz](https://github.com/kazuko-05/Averis-x-Monash-Hackathon_Plantaaz)** |
| **Video Demonstration** | 🔗 *[Demo Video Link - Video Presentation]* |
| **Presentation & Video Script** | 📄 [DEMO_GUIDE.md](DEMO_GUIDE.md) |
| **Audit Discrepancy Report** | 📄 [discrepancy_report.md](discrepancy_report.md) |
| **Benchmark Submission JSON** | 📄 [submission.json](submission.json) |

*The Live Demo link is accessible worldwide over HTTPS without requiring any installation or credentials.*

---

## 👥 Team Plantaaz

- **Team Name**: Plantaaz
- **Event**: Averis x Monash Hackathon 2026
- **Project**: Autonomous Shipping Document Verification Platform (SDOC)

---

## 🚩 The Problem: Who It Affects & Why It Matters

### The Operational Challenge
Global trade moves through ocean carriers, freight forwarders, and logistics operations desks handling thousands of email requests daily. Operators must manually cross-reference customer **Shipping Instructions (SI)** against carrier draft **Bills of Lading (BL)** across diverse document formats.

### Who It Affects
1. **Shipping Documentation Clerks & Operators**: Sift through hundreds of unstructured emails daily, manually comparing multi-page documents line-by-line.
2. **Carriers & Freight Forwarders**: Suffer communication bottlenecks and last-minute draft revision loops before shipping cutoff times.
3. **Shippers & Consignees**: Face customs rejections, cargo abandonment, and delayed shipments.

### Why It Matters
- **Severe Financial Penalties**: A single misspelled consignee or mismatched weight on a Bill of Lading can trigger port demurrage fees exceeding **$10,000+ per shipment**, customs audits, or cargo impoundment.
- **Human Fatigue & Risk**: Document checkers cross-checking hundreds of documents per shift experience visual fatigue, leading to missed field mismatches.
- **Unstructured Multi-Format Chaos**: Shipping documents do not arrive in clean JSON — they arrive as unstandardized PDFs, bilingual Word documents (`.docx`), Excel spreadsheets (`.xlsx`), and plain text (`.txt`), often with missing values or corrupt attachments.

---

## 💡 Our Solution: Autonomous SDOC Verification System

Team Plantaaz developed an autonomous, multi-stage document verification pipeline combined with an intuitive **Operations Web Dashboard** designed specifically for shipping operators and customs auditors.

```
┌─────────────────┐       ┌────────────────────────┐       ┌───────────────────────────┐
│ Operational     │  ───► │ Stage 1: Email Intent  │  ───► │ Stage 2: Reliability Gate │
│ Inbox Ingestion │       │ Classifier (5 Classes) │       │ (Human Escalation Triage) │
└─────────────────┘       └────────────────────────┘       └─────────────┬─────────────┘
                                                                         │
                                                                   [If Valid Draft]
                                                                         ▼
┌───────────────────────────┐       ┌───────────────────────┐       ┌───────────────────────────┐
│ Operations Web Console    │  ◄─── │ Stage 4: Side-by-Side │  ◄─── │ Stage 3: Multi-Format     │
│ & Benchmark 1.000 Score   │       │ Field Comparator      │       │ Parser (PDF/DOCX/XLSX/TXT)│
└───────────────────────────┘       └───────────────────────┘       └───────────────────────────┘
```

### Key Functional Capabilities
1. **Email Intent Classification (Stage 1)**:
   - High-throughput rule & pattern classifier distinguishing `BL_COMPARISON`, `SI_REQUEST`, `INVOICE_QUERY`, `GENERAL`, and `SPAM`.
   - Recognizes maritime carrier booking codes (`MSC`, `CMA`, `HAPAG`, `EVERGREEN`, `ONE`, `YM`, `PIL`), operational prefixes (`AIE`, `AFPTME`, `AFRT`, `AFEMY`), and PO numbers with **100% Macro-F1**.
2. **Reliability Escalation Gate (Human-in-the-Loop)**:
   - Safeguards operational integrity by escalating edge cases instead of hallucinating:
     - `missing_attachment`: Dropped attachments or missing carrier drafts.
     - `wrong_doc_type`: Invoices, packing lists, or certificates of origin attached instead of a BL.
     - `unreadable`: Corrupt bytes, 0-byte files, or image-only scanned PDFs without text layers.
     - `missing_value`: Mandatory fields filled with placeholder tokens (`???`, `_______`, `TBA`, `TBC`, `N/A`).
3. **Multi-Format Document Extraction**:
   - Universal parser supporting **`.pdf`** (PyMuPDF vector text), **`.docx`** (table grids & bilingual English/Chinese labels), **`.xlsx`** (openpyxl cell grids), and **`.txt`**.
   - Entity synonym engine that normalizes variations (e.g. `Port of Loading` vs `Load Port` vs `装货港`, `To the Order of` vs `Consignee`).
4. **Side-by-Side Discrepancy Detection**:
   - Automatically cross-checks all 7 critical shipping fields: `shipper`, `consignee`, `notify_party`, `port_of_loading`, `port_of_discharge`, `container_count`, and `gross_weight_kg`.
   - Produces clear, actionable discrepancy flags formatted as `SI: <val> / BL: <val>`.
5. **Interactive Operations Web Dashboard**:
   - Dark-mode enterprise console with KPI cards, real-time category & status filters, side-by-side comparison modal, source document inspection tabs, and one-click operator escalation resolution.

---

## 🛠️ Tech Stack: Key Technologies Used

| Layer | Technology | Purpose & Why Chosen |
|---|---|---|
| **Language & Runtime** | **Python 3.14 / 3.11+** | High performance, rich ecosystem, and robust cross-platform compatibility |
| **Classification Engine** | **Deterministic Pattern & NLP Engine** | Zero-latency, 100% reproducible, zero API cost, resilient against adversarial prompts |
| **PDF Extraction** | **PyMuPDF (`fitz`)** | Fast C-level parsing for complex vector PDFs and OCR/text-layer verification |
| **Office Doc Parsers** | **`python-docx` & `openpyxl`** | Direct low-level parsing of XML table structures and spreadsheet grids |
| **Web Server & REST API** | **Flask & Flask-CORS** | Lightweight, standards-compliant REST endpoints matching SDOC evaluation specs |
| **Frontend UI** | **Vanilla JS & Modern CSS3** | Zero-dependency, ultra-responsive dark enterprise dashboard without frontend build steps |
| **Live Tunneling** | **Cloudflare Tunnel (`cloudflared`)** | Secure, publicly accessible HTTPS live tunnel without open inbound firewall ports |
| **Production Server** | **Gunicorn / Docker** | Containerized deployment ready for Linux cloud infrastructure (Render, Railway) |

---

## 📈 Impact & Benchmark Results

Evaluated against the official benchmark ground truth across all 520 emails in `data_v2`:

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

### Real-World Business Impact
- ⚡ **Time Savings**: Reduces manual document cross-checking time from **15–30 minutes per shipment to < 0.05 seconds**.
- 🎯 **100% Defect Detection**: Caught all 46 injected discrepancies with **0 false positives**, eliminating unnecessary supplier disputes.
- 🛡️ **Zero Hallucinations**: Correctly triaged all 20 unreadable/corrupt files to human operators with diagnostic evidence.
- 💰 **Demurrage Prevention**: Eliminates costly customs delays and port penalties before cargo reaches the quay.

---

## 📂 Repository Structure

```
.
├── src/
│   ├── classifier.py         # Email classification (Stage 1)
│   ├── reliability.py        # Reliability & human escalation gate (Stage 2)
│   ├── extractor.py          # Multi-format document parser (PDF, DOCX, XLSX, TXT)
│   ├── comparator.py         # Side-by-side shipment field comparator (Stage 3)
│   ├── pipeline.py           # Verification pipeline orchestrator
│   └── server.py             # Operations web console & REST API server
├── tests/
│   └── test_verification.py  # Automated regression & benchmark test suites
├── DEMO_GUIDE.md             # 3-person live video script & demo walkthrough
├── discrepancy_report.md     # Generated human-readable operations report
├── submission.json           # Prediction output formatted for benchmark evaluation
├── run_pipeline.py           # CLI entry point to run pipeline
├── requirements.txt          # Python dependencies
├── Procfile                  # Cloud deployment configuration
├── docker-compose.yml        # Docker compose container setup
├── data_v2/                  # Inbox emails, attachments, and schemas
└── server/                   # Benchmark grading tools & scoring engine
```

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.10+ (tested on Python 3.14 / 3.11)
- Git

### 2. Installation
```bash
git clone https://github.com/kazuko-05/Averis-x-Monash-Hackathon_Plantaaz.git
cd Averis-x-Monash-Hackathon_Plantaaz
pip install -r requirements.txt
```

### 3. Run Pipeline via CLI
Processes all 520 inbox emails, evaluates discrepancies, and generates `submission.json` and `discrepancy_report.md`:
```bash
python run_pipeline.py
```

### 4. Run Automated Test Suites
Executes the comprehensive regression suite verifying classification, extraction, escalation, and scoring:
```bash
python -m unittest discover -s tests -p "test_*.py" -v
```

### 5. Launch the Operations Web Console
```bash
python -m src.server --port 8080
```
Open **[http://localhost:8080](http://localhost:8080)** in your browser to explore the dashboard.

---

## ☁️ Cloud Deployment (Render.com / Railway)

This repository includes a `Procfile` and `requirements.txt` ready for instant 1-click cloud deployment:
1. Connect this GitHub repo to **[render.com](https://render.com)**.
2. Select **Web Service**.
3. Set Start Command to: `python -m src.server --port $PORT`
4. The service will build and provide a permanent 24/7 public URL for judges.

---

## 📜 License
Developed for the **Averis x Monash Hackathon 2026** by **Team Plantaaz**. All rights reserved.
