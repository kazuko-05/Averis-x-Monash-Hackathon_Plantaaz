"""
Shipment Comparator Module.

Performs side-by-side comparison between Shipping Instructions (SI) and draft
Bills of Lading (BL) across 7 canonical shipping fields:
1. shipper
2. consignee
3. notify_party
4. port_of_loading
5. port_of_discharge
6. container_count
7. gross_weight_kg
"""

from typing import Dict, Any, List, Tuple

COMPARE_FIELDS = [
    "shipper",
    "consignee",
    "notify_party",
    "port_of_loading",
    "port_of_discharge",
    "container_count",
    "gross_weight_kg",
]


class ShipmentComparator:
    """Compares SI and BL data dictionaries and generates discrepancy reports."""

    def compare(
        self, si_data: Dict[str, Any], bl_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Compares extracted SI and BL field values.

        Returns:
            Dict containing:
            - status: 'OK' or 'MISMATCH'
            - has_defect: bool
            - defect_fields: List[str]
            - discrepancies: List[Dict[str, Any]] (side-by-side details)
            - summary: str
        """
        defect_fields: List[str] = []
        discrepancies: List[Dict[str, Any]] = []

        for field in COMPARE_FIELDS:
            s_val = si_data.get(field)
            b_val = bl_data.get(field)

            # Both values present and disagree
            if s_val is not None and b_val is not None:
                if s_val != b_val:
                    defect_fields.append(field)
                    discrepancies.append({
                        "field": field,
                        "si_value": s_val,
                        "bl_value": b_val,
                        "display": f"SI: {s_val} / BL: {b_val}",
                    })

        has_defect = len(defect_fields) > 0
        defect_fields = sorted(defect_fields)

        if not has_defect:
            summary = "No mismatch detected."
        else:
            diff_strs = [d["display"] for d in discrepancies]
            summary = f"{len(defect_fields)} mismatch(es) detected: {', '.join(defect_fields)} ({'; '.join(diff_strs)})"

        return {
            "status": "MISMATCH" if has_defect else "OK",
            "has_defect": has_defect,
            "defect_fields": defect_fields,
            "discrepancies": discrepancies,
            "summary": summary,
            "si_data": si_data,
            "bl_data": bl_data,
        }
