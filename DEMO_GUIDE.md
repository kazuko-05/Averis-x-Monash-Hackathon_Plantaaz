# 🎬 SDOC Verification System — Live Demo & Presentation Guide

This guide explains how to **demonstrate the working application** and walk judges or users through the end-to-end user experience.

---

## 🚀 How to Launch the Application

1. Open PowerShell and navigate to the project directory:
   ```powershell
   cd C:\Users\Kuhan\Downloads\Hackathon
   ```
2. Start the interactive console:
   ```powershell
   $env:PYTHONIOENCODING="utf-8"
   & "C:\msys64\ucrt64\bin\python.exe" -m src.server --port 8080
   ```
3. In your web browser, open:
   👉 **[http://localhost:8080](http://localhost:8080)**

---

## 🎯 3-Minute Live Demo Walkthrough (Step-by-Step)

### Step 1: High-Level Operational Overview (30s)
- **What to show**: The top KPI summary cards and the live status badge.
- **What to say**:
  > *"Shipping operations teams receive hundreds of mixed emails daily—including document check requests, invoice queries, and spam. Our system automatically ingests and triages the entire inbox of 520 emails in real-time, achieving a 100% benchmark score. Out of 220 Bill of Lading verification requests, it caught all 46 injected defects with 0 false alarms, and escalated 20 ambiguous cases to the human operations queue."*

---

### Step 2: Discrepancy Detection & Side-by-Side Comparison (45s)
- **What to click**:
  - Click the **`🔴 Discrepancy (Email 004)`** demo preset button at the top, OR
  - Click the **`Mismatch (46)`** status filter in the toolbar and click on **`email_004`**.
- **What to show**:
  - The modal drawer opens displaying:
    - Original email subject and sender.
    - The **Shipment Field Comparison** table.
    - Highlighted in red:
      - `Consignee`: **SI**: `EAST BRIGHT FZ-LLC` vs **BL**: `UAB NOVAKOPA`
      - `Notify Party`: **SI**: `EAST BRIGHT FZ-LLC` vs **BL**: `UAB NOVAKOPA`
    - Click the **`📄 Source Documents Text`** tab in the modal to reveal the raw extracted text of the SI and BL side-by-side!
- **What to say**:
  > *"When a document-checking email arrives, the system extracts the 7 critical shipping fields: shipper, consignee, notify party, port of loading, port of discharge, container count, and gross weight. Here on email_004, the system caught a consignee mismatch between the customer's SI and the carrier's draft BL before cargo was loaded, preventing costly customs penalties."*

---

### Step 3: Multi-Format Support (PDF, Word DOCX, Excel XLSX) (30s)
- **What to click**:
  - Click the **`🟡 Multi-Format DOCX/XLSX (Email 055)`** demo preset button.
- **What to show**:
  - Point out that the SI was an Excel spreadsheet (`.xlsx`) and the BL was a bilingual Word document (`.docx` with Chinese and English labels like `装货港` and `毛重`).
  - Show how label synonyms (`Port of Loading (POL)` vs `PORT OF LOADING (装货港)`) were automatically normalized.
- **What to say**:
  > *"In the real world, documents don't arrive in plain text. Our system features native multi-format parsers supporting PDFs, bilingual Word documents, and Excel spreadsheets. It uses an entity synonym engine to recognize that 'Load Port' and 'Port of Loading' refer to the exact same field."*

---

### Step 4: Clean Document Verification (20s)
- **What to click**:
  - Click the **`🟢 Clean Match (Email 001)`** demo preset button.
- **What to show**:
  - Point out the green status badge: **`OK`** and the summary: `"No mismatch detected."`
  - All 7 fields in the side-by-side table display green `MATCH` badges.
- **What to say**:
  > *"When all seven fields agree, the draft is instantly cleared for finalization with 'No mismatch detected', saving shipping documentation staff hours of repetitive manual cross-checking."*

---

### Step 5: Reliability & Human-in-the-Loop Escalation (45s)
- **What to click**:
  - Click the **`⚠️ Wrong Doc Type (Email 501)`** demo preset button.
  - Or click **`⚠️ Unreadable Scan (Email 512)`** or **`⚠️ Missing Value (Email 516)`**.
- **What to show**:
  - Status badge: **`NEEDS_REVIEW (wrong_doc_type)`**.
  - Notice the warning box:
    - *"Reason Code: wrong_doc_type"*
    - *"Evidence Context: Attachment email_501_BL.txt is a Commercial Invoice, not a draft Bill of Lading."*
  - Show the interactive operator action buttons:
    - `[Confirm Rejection]`
    - `[Approve As Exception]`
    - `[Request Re-upload]`
  - Click **Confirm Rejection** &rarr; An alert confirms the case is resolved and logged!
- **What to say**:
  > *"A truly reliable autonomous system must know when NOT to guess. When an unreadable scanned PDF, an empty file, a wrong document type like an invoice, or blank fields arrive, the system does not hallucinate. Instead, it escalates directly to a human operator with clear evidence and allows one-click action to request re-upload or resolve."*

---

### Step 6: Live Benchmark Scoreboard (20s)
- **What to click**:
  - Click the green **`🏆 View Scoreboard`** button in the header.
- **What to show**:
  - The official scoreboard modal opens displaying:
    - **Overall Weighted Score: `1.0000 / 1.0000` (100%)**
    - **Stage 1 (Classification Macro-F1)**: `100.0%`
    - **Stage 3 (Defect Catch F1)**: `100.0%`
    - **Reliability (Escalation Recall)**: `100.0%` (0 false alarms)
    - **End-to-End Defect Rate**: `100.0%` (46/46 defects caught)
- **What to say**:
  > *"Finally, we evaluated our pipeline against the official benchmark ground truth. The system achieved a perfect 1.0000 score across all stages, establishing an optimal balance of accuracy, format flexibility, and operational safety."*

---

## 📋 Summary of Key User Interactions

| User Role | User Action | System Response |
|---|---|---|
| **Operations Staff** | Opens Console Dashboard | Displays real-time KPI overview and categorised email queue |
| **Document Checker** | Clicks on any email with mismatches | Opens side-by-side comparison table with red highlight on discrepancies |
| **Document Checker** | Clicks "Source Documents Text" tab | Displays raw text of SI vs draft BL side-by-side |
| **Reviewer (HITL)** | Inspects escalated case | Displays escalation reason code and evidence (e.g. wrong doc, unreadable scan) |
| **Reviewer (HITL)** | Clicks action (e.g. "Request Re-upload") | Resolves the case and updates the operational log |
| **Manager / Auditor** | Clicks "View Discrepancy Report" | Opens formatted markdown discrepancy report for export or audit |
| **Evaluator / Judge** | Clicks "View Scoreboard" | Displays live evaluation metrics against private benchmark |
