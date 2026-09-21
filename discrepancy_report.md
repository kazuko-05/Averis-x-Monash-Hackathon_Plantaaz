# Shipping Document Verification - Discrepancy & Operational Report

## Executive Summary
- **Total Emails Ingested**: 520
- **BL Document Checks**: 220
  - **Discrepancies Caught (MISMATCH)**: 46
  - **Clean Matches (OK)**: 154
  - **Escalated to Human Review (NEEDS_REVIEW)**: 20
- **SI Requests**: 125
- **Invoice Queries**: 75
- **General Updates**: 60
- **Spam Filtered**: 40

---

## Document Comparison Discrepancies (Immediate Attention Required)

| Email ID | Subject | Mismatched Fields | Side-by-Side Values (SI vs BL) |
|---|---|---|---|
| `email_004` | REQUEST BL DRAFT _ PO 26067_ COATED IVORY BOARD__138MT | consignee, notify_party | **consignee**: SI: EAST BRIGHT FZ-LLC / BL: UAB NOVAKOPA<br>**notify_party**: SI: EAST BRIGHT FZ-LLC / BL: UAB NOVAKOPA |
| `email_013` | AFEMY - MOMBASA_KENYA - CMA(SIJ4216073) - 5RFR-36541 - 5250074586 - ROXCEL TRADING GMBH - OA_CFR | port_of_discharge | **port_of_discharge**: SI: MOMBASA / BL: TUTICORIN |
| `email_025` | RE_ TO CONFIRM DOCS _ 5SUS-86999 _ FREMANTLE_AUSTRALIA _ CERIEX _ SIN204711671 | container_count, port_of_discharge | **port_of_discharge**: SI: FREMANTLE / BL: BUSAN<br>**container_count**: SI: 6 / BL: 5 |
| `email_031` | AFEMY - MOMBASA_KENYA - ONE(SINF87558867) - 5RCY-36057 - 5250076627 - VITAL SOLUTIONS PTE. LTD. - DP | container_count, gross_weight_kg | **container_count**: SI: 1 / BL: 3<br>**gross_weight_kg**: SI: 21114 / BL: 23114 |
| `email_043` | RE_ AFRT - KLAIPEDA_LITHUANIA - CMA(SIJ5991022) - 5RAE-97643 - 5250078156 - PACIFIC OFFICE (M) SDN BHD - OA_CFR | container_count | **container_count**: SI: 3 / BL: 5 |
| `email_046` | RE_ AFEMY - SAVANNAH_US - EVER(EGLV552312432921) - 5ALT-79955 - 5250072717 - SAFQA LIMITED - OA_CFR | notify_party | **notify_party**: SI: TOPKOPY MIDDLE EAST FZE / BL: MOORIM SP CO., LTD |
| `email_065` | RE_ AFEMY - HOCHIMINH CITY_VIETNAM - PIL(SIN742054932) - 5RMY-27530 - 5250074637 - INTERNATIONAL FOREST PRODUCTS LLC - DP | notify_party, port_of_discharge | **notify_party**: SI: INTERNATIONAL FOREST PRODUCTS LLC / BL: HABRAS INTERNATIONAL LIMITED<br>**port_of_discharge**: SI: HOCHIMINH CITY / BL: BUSAN |
| `email_071` | RE_ REQUEST BL DRAFT _ PO 25451_ COATED IVORY BOARD__132MT | container_count, port_of_discharge | **port_of_discharge**: SI: YANGON / BL: CEBU<br>**container_count**: SI: 6 / BL: 8 |
| `email_091` | RE_ TO CONFIRM DOCS _ 5RUS-26221 _ CALLAO_PERU _ ORIENT LINKS CO (LLC) _ HLCUSIN700516271 | container_count | **container_count**: SI: 3 / BL: 2 |
| `email_097` | Draft BL MARCOPOLO 810 V.BS005 SINGAPORE - amend BL 055 | container_count, gross_weight_kg | **container_count**: SI: 10 / BL: 11<br>**gross_weight_kg**: SI: 216950 / BL: 215950 |
| `email_107` | TO CONFIRM DOCS _ 5RFR-36884 _ MOMBASA_KENYA _ KTP CO., LTD _ OOLU1815997062 | consignee, container_count | **consignee**: SI: KTP CO., LTD / BL: VITAL SOLUTIONS PTE. LTD.<br>**container_count**: SI: 2 / BL: 3 |
| `email_111` | AIE - APAPA_NIGERIA - CMA(SIJ2999119) - 5RSG-79970 - 5250072462 - CLIFFORD PAPER INC - DP | container_count | **container_count**: SI: 4 / BL: 3 |
| `email_119` | TO CONFIRM DOCS _ 5APH-57532 _ SAVANNAH_US _ CLIFFORD PAPER INC _ MEDUUD104478 | port_of_loading | **port_of_loading**: SI: PORT KLANG (WESTPORT) / BL: SINGAPORE |
| `email_121` | TO CONFIRM DOCS _ 5RAE-73753 _ BRISBANE_AUSTRALIA _ CLIFFORD PAPER INC _ MCLSIN3934835 | gross_weight_kg | **gross_weight_kg**: SI: 20842 / BL: 21342 |
| `email_128` | TO CONFIRM DOCS _ 5AKR-72269 _ NEW YORK_US _ BALL & DOGGETT AUSTRALIA PTY LTD _ MCLSIN9958669 | gross_weight_kg, port_of_loading | **port_of_loading**: SI: NHAVA SHEVA / BL: BUATAN<br>**gross_weight_kg**: SI: 323250 / BL: 322250 |
| `email_129` | REQUEST BL DRAFT _ PO 26680_ COATED IVORY BOARD__126MT | port_of_discharge, port_of_loading | **port_of_loading**: SI: NHAVA SHEVA / BL: BUATAN<br>**port_of_discharge**: SI: ASHDOD / BL: TUTICORIN |
| `email_133` | AFPTME - CALLAO_PERU - EVER(EGLV801573993056) - 5APH-08588 - 5250077704 - MOORIM SP CO., LTD - OA | gross_weight_kg | **gross_weight_kg**: SI: 142848 / BL: 144848 |
| `email_144` | TO CONFIRM DOCS _ 5RMY-98643 _ MERSIN_TURKEY _ NAGAPPA EXPORTS _ HLCUSIN086376599 | consignee, container_count | **consignee**: SI: NAGAPPA EXPORTS / BL: PACIFIC OFFICE (M) SDN BHD<br>**container_count**: SI: 12 / BL: 11 |
| `email_145` | RE_ TO CONFIRM DOCS _ 5RSG-68872 _ BUSAN_SOUTH KOREA _ PACIFIC OFFICE (M) SDN BHD _ MCLSIN6944869 | shipper | **shipper**: SI: APRIL FINE PAPER TRADING / BL: APRIL FINE PAPER TRADING (MIDDLE EAST) FZE |
| `email_174` | RE_ TO CONFIRM DOCS _ 5RMY-99499 _ CONAKRY_GUINEA _ TOAN LUC PAPER JOINT STOCK COMPANY _ OOLU1252056647 | notify_party, port_of_discharge | **notify_party**: SI: TOAN LUC PAPER JOINT STOCK COMPANY / BL: MOORIM SP CO., LTD<br>**port_of_discharge**: SI: CONAKRY / BL: HOCHIMINH CITY |
| `email_178` | RE_ TO CONFIRM DOCS _ 5RMY-40777 _ CALLAO_PERU _ ORIENT LINKS CO (LLC) _ SIJ2206447 | container_count | **container_count**: SI: 6 / BL: 7 |
| `email_182` | RE_ Draft BL VISION 202 V.002 NANTONG - amend BL 041 | container_count, port_of_discharge | **port_of_discharge**: SI: APAPA / BL: BALTIMORE<br>**container_count**: SI: 5 / BL: 6 |
| `email_225` | AFRT - GDANSK_POLAND - PIL(SIN556503334) - 5RMY-50769 - 5250078640 - ROXCEL TRADING GMBH - LC | consignee | **consignee**: SI: ROXCEL TRADING GMBH / BL: AL GURG STATIONERY LLC |
| `email_243` | RE_ Draft BL INDO SUKSES 65 V.51NW1 PORT KLANG (WESTPORT) - amend BL 055 | port_of_discharge, port_of_loading | **port_of_loading**: SI: PORT KLANG (WESTPORT) / BL: RUGAO/NANTONG/SHANGHAI<br>**port_of_discharge**: SI: HOUSTON / BL: MOMBASA |
| `email_256` | RE_ REQUEST BL DRAFT _ PO 26033_ PAPERBOARD__300MT | port_of_discharge, shipper | **shipper**: SI: APRIL FINE PAPER TRADING / BL: APRIL FAR EAST (M) SDN BHD<br>**port_of_discharge**: SI: VALPARAISO / BL: FREMANTLE |
| `email_270` | AIE - MERSIN_TURKEY - CMA(SIJ5304289) - 5RCY-86857 - 5250078725 - KPP-ANTALIS (SINGAPORE) PTE. LTD. - LC | port_of_discharge | **port_of_discharge**: SI: MERSIN / BL: LONG BEACH |
| `email_291` | RE_ TO CONFIRM DOCS _ 5RMY-12871 _ SAVANNAH_US _ INTERNATIONAL FOREST PRODUCTS LLC _ OOLU7833321160 | consignee, container_count | **consignee**: SI: INTERNATIONAL FOREST PRODUCTS LLC / BL: TOPKOPY MIDDLE EAST FZE<br>**container_count**: SI: 1 / BL: 3 |
| `email_300` | AFEMY - VALPARAISO_CHILE - HAPAG(HLCUSIN186151554) - 5RFR-11284 - 5250079718 - SAFQA LIMITED - CFR | notify_party, shipper | **shipper**: SI: APRIL FAR EAST (M) SDN BHD / BL: APRIL FINE PAPER TRADING (MIDDLE EAST) FZE<br>**notify_party**: SI: UAB NOVAKOPA / BL: NAGAPPA EXPORTS |
| `email_302` | RE_ Draft BL SOLID 16 V.044NW2 RUGAO/NANTONG/SHANGHAI - amend BL 052 | container_count | **container_count**: SI: 2 / BL: 4 |
| `email_312` | REQUEST BL DRAFT _ PO 26052_ COATED IVORY BOARD__220MT | notify_party, shipper | **shipper**: SI: APRIL FINE PAPER TRADING (MIDDLE EAST) FZE / BL: APRIL FAR EAST (M) SDN BHD<br>**notify_party**: SI: 3S PAPER PRODUCTS SDN BHD / BL: KPP-ANTALIS (SINGAPORE) PTE. LTD. |
| `email_313` | RE_ AFEMY - HOCHIMINH CITY_VIETNAM - MSC(MEDUUD649837) - 5RMY-62736 - 5250075271 - KPP-ANTALIS (SINGAPORE) PTE. LTD. - OA_CFR | container_count, gross_weight_kg | **container_count**: SI: 5 / BL: 4<br>**gross_weight_kg**: SI: 118270 / BL: 117770 |
| `email_324` | RE_ AFEMY - NEW YORK_US - PIL(SIN597371470) - 5RMY-60567 - 5250073030 - CLIFFORD PAPER INC - DP | container_count, shipper | **shipper**: SI: ASIA PACIFIC PAPERBOARD TRADING PTE LTD / BL: APRIL FAR EAST (M) SDN BHD<br>**container_count**: SI: 3 / BL: 4 |
| `email_334` | RE_ REQUEST BL DRAFT _ PO 26324_ FUJITO PAPERONE INKJET PAPER__138MT | consignee, shipper | **shipper**: SI: ASIA PACIFIC PAPERBOARD TRADING PTE LTD / BL: APRIL FINE PAPER TRADING<br>**consignee**: SI: EAST BRIGHT FZ-LLC / BL: INTERNATIONAL FOREST PRODUCTS LLC |
| `email_342` | TO CONFIRM DOCS _ 5AAT-96661 _ AQABA_JORDAN _ MOORIM SP CO., LTD _ YMJAI861031310 | container_count, notify_party | **notify_party**: SI: HABRAS INTERNATIONAL LIMITED / BL: SAFQA LIMITED<br>**container_count**: SI: 1 / BL: 2 |
| `email_351` | RE_ TO CONFIRM DOCS _ 5RCY-19754 _ ASHDOD_ISRAEL _ KTP CO., LTD _ SIN979162022 | container_count, gross_weight_kg | **container_count**: SI: 15 / BL: 16<br>**gross_weight_kg**: SI: 359415 / BL: 360415 |
| `email_354` | TO CONFIRM DOCS _ 5RSG-78360 _ VALPARAISO_CHILE _ HABRAS INTERNATIONAL LIMITED _ OOLU4901495427 | gross_weight_kg, notify_party | **notify_party**: SI: HABRAS INTERNATIONAL LIMITED / BL: NAGAPPA EXPORTS<br>**gross_weight_kg**: SI: 20603 / BL: 22603 |
| `email_361` | TO CONFIRM DOCS _ 5RSG-98645 _ BRISBANE_AUSTRALIA _ PACIFIC OFFICE (M) SDN BHD _ EGLV765728941347 | gross_weight_kg, port_of_discharge | **port_of_discharge**: SI: BRISBANE / BL: MOMBASA<br>**gross_weight_kg**: SI: 239590 / BL: 238590 |
| `email_379` | TO CONFIRM DOCS _ 5RUS-90203 _ HOUSTON_US _ ROXCEL TRADING GMBH _ EGLV485157919711 | shipper | **shipper**: SI: APRIL FAR EAST (M) SDN BHD / BL: APRIL FINE PAPER TRADING |
| `email_410` | REQUEST BL DRAFT _ PO 26446_ PAPERONE DIGITAL COPIER PAPER__315MT | port_of_loading | **port_of_loading**: SI: SINGAPORE / BL: PORT KLANG (WESTPORT) |
| `email_416` | AIE - LONG BEACH_US - EVER(EGLV585125389218) - 5RCY-35837 - 5250074907 - VITAL SOLUTIONS PTE. LTD. - DP | gross_weight_kg | **gross_weight_kg**: SI: 105625 / BL: 106625 |
| `email_426` | RE_ AIE - NEW YORK_US - MONTER(MCLSIN8077113) - 5SUS-36957 - 5250072790 - KTP CO., LTD - OA | container_count, port_of_discharge | **port_of_discharge**: SI: NEW YORK / BL: KLAIPEDA<br>**container_count**: SI: 10 / BL: 11 |
| `email_434` | RE_ TO CONFIRM DOCS _ 5ALT-34476 _ BUSAN_SOUTH KOREA _ TOPKOPY MIDDLE EAST FZE _ YMJAI970996254 | port_of_discharge | **port_of_discharge**: SI: BUSAN / BL: CEBU |
| `email_435` | RE_ AFPTME - AQABA_JORDAN - EVER(EGLV353574859532) - 5RMY-33797 - 5250070581 - AL GURG STATIONERY LLC - DP | gross_weight_kg | **gross_weight_kg**: SI: 214270 / BL: 214770 |
| `email_468` | TO CONFIRM DOCS _ 5ALT-45057 _ ASHDOD_ISRAEL _ ROXCEL TRADING GMBH _ MCLSIN2031954 | container_count, port_of_loading | **port_of_loading**: SI: SINGAPORE / BL: RUGAO/NANTONG/SHANGHAI<br>**container_count**: SI: 1 / BL: 3 |
| `email_481` | RE_ AFRT - VALPARAISO_CHILE - CMA(SIJ6060148) - 5AKR-79388 - 5250074136 - AL GURG STATIONERY LLC - OA_CFR | consignee | **consignee**: SI: AL GURG STATIONERY LLC / BL: 3S PAPER PRODUCTS SDN BHD |
| `email_499` | RE_ AIE - HOCHIMINH CITY_VIETNAM - MSC(MEDUUD646871) - 5RUS-81876 - 5250079208 - TOPKOPY MIDDLE EAST FZE - OA | gross_weight_kg | **gross_weight_kg**: SI: 40326 / BL: 41326 |

---

## Human Review Queue (Escalated Cases)

| Email ID | Escalation Reason | Evidence / Context | Recommended Operator Action |
|---|---|---|---|
| `email_501` | `wrong_doc_type` | Attachment attachments/email_501_BL.txt is a Commercial Invoice, not a draft Bill of Lading. | Request draft Bill of Lading from customer/agent; current attachment is non-BL. |
| `email_502` | `wrong_doc_type` | Attachment attachments/email_502_BL.txt is a Packing List, not a draft Bill of Lading. | Request draft Bill of Lading from customer/agent; current attachment is non-BL. |
| `email_503` | `wrong_doc_type` | Attachment attachments/email_503_BL.txt is a Certificate of Origin, not a draft Bill of Lading. | Request draft Bill of Lading from customer/agent; current attachment is non-BL. |
| `email_504` | `wrong_doc_type` | Attachment attachments/email_504_BL.txt is a Packing List, not a draft Bill of Lading. | Request draft Bill of Lading from customer/agent; current attachment is non-BL. |
| `email_505` | `wrong_doc_type` | Attachment attachments/email_505_BL.txt is a Certificate of Origin, not a draft Bill of Lading. | Request draft Bill of Lading from customer/agent; current attachment is non-BL. |
| `email_506` | `missing_attachment` | Email indicates attachments were intended but none were attached. | Contact sender to re-attach dropped draft BL or verify thread attachments. |
| `email_507` | `missing_attachment` | Only one attachment provided (expected SI and draft BL pair). | Contact sender to re-attach dropped draft BL or verify thread attachments. |
| `email_508` | `missing_attachment` | Email indicates attachments were intended but none were attached. | Contact sender to re-attach dropped draft BL or verify thread attachments. |
| `email_509` | `missing_attachment` | Only one attachment provided (expected SI and draft BL pair). | Contact sender to re-attach dropped draft BL or verify thread attachments. |
| `email_510` | `missing_attachment` | Email indicates attachments were intended but none were attached. | Contact sender to re-attach dropped draft BL or verify thread attachments. |
| `email_511` | `unreadable` | Failed to parse PDF document attachments/email_511_BL.pdf: Failed to open file 'data_v2\\attachments\\email_511_BL.pdf'. | Route to OCR engine or request higher resolution non-corrupt document. |
| `email_512` | `unreadable` | Scanned image PDF without machine-readable text layer: attachments/email_512_SI.pdf | Route to OCR engine or request higher resolution non-corrupt document. |
| `email_513` | `unreadable` | Scanned image PDF without machine-readable text layer: attachments/email_513_SI.pdf | Route to OCR engine or request higher resolution non-corrupt document. |
| `email_514` | `unreadable` | Scanned image PDF without machine-readable text layer: attachments/email_514_SI.pdf | Route to OCR engine or request higher resolution non-corrupt document. |
| `email_515` | `unreadable` | Failed to parse PDF document attachments/email_515_BL.pdf: Failed to open file 'data_v2\\attachments\\email_515_BL.pdf'. | Route to OCR engine or request higher resolution non-corrupt document. |
| `email_516` | `missing_value` | Required field 'Gross Weight毛重(KGS)' in attachments/email_516_SI.txt has blank or unpopulated token: 'N/A' | Contact shipper/customer to populate blank mandatory fields before re-check. |
| `email_517` | `missing_value` | Required field 'Port of Loading (POL)' in attachments/email_517_SI.txt has blank or unpopulated token: '____MT' | Contact shipper/customer to populate blank mandatory fields before re-check. |
| `email_518` | `missing_value` | Required field 'PORT OF DISCHARGE' in attachments/email_518_SI.txt has blank or unpopulated token: 'N/A' | Contact shipper/customer to populate blank mandatory fields before re-check. |
| `email_519` | `missing_value` | Required field 'SHIPPER' in attachments/email_519_SI.txt has blank or unpopulated token: '' | Contact shipper/customer to populate blank mandatory fields before re-check. |
| `email_520` | `missing_value` | Required field 'CONSIGNEE' in attachments/email_520_SI.txt has blank or unpopulated token: '' | Contact shipper/customer to populate blank mandatory fields before re-check. |

---

*Report generated autonomously by SDOC Verification Pipeline.*
