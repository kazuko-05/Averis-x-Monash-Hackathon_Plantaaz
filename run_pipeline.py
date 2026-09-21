#!/usr/bin/env python3
"""
CLI runner for the Shipping Document Verification Pipeline.

Usage:
    python run_pipeline.py [--data data_v2] [--submission submission.json] [--report discrepancy_report.md]
"""

import argparse
import sys
from pathlib import Path

# Add workspace to path
WORKSPACE_ROOT = Path(__file__).resolve().parent
if str(WORKSPACE_ROOT) not in sys.path:
    sys.path.insert(0, str(WORKSPACE_ROOT))

from src.pipeline import VerificationPipeline
from server import scoring


def main():
    parser = argparse.ArgumentParser(description="Run Shipping Document Verification Pipeline.")
    parser.add_argument("--data", default="data_v2", help="Path to dataset directory containing inbox/ and attachments/")
    parser.add_argument("--submission", default="submission.json", help="Path to output submission JSON")
    parser.add_argument("--report", default="discrepancy_report.md", help="Path to output discrepancy markdown report")
    args = parser.parse_args()

    print("=" * 66)
    print("  SHIPPING DOCUMENT VERIFICATION PIPELINE")
    print(f"  Dataset: {args.data}")
    print("=" * 66)

    pipeline = VerificationPipeline(data_root=args.data)

    print("\n[1/4] Processing inbox emails through verification pipeline...")
    submission, records = pipeline.process_inbox()
    print(f"      Processed {len(records)} emails.")

    print(f"\n[2/4] Saving submission format to {args.submission}...")
    pipeline.save_submission(submission, output_path=args.submission)

    print(f"\n[3/4] Generating operational discrepancy report to {args.report}...")
    pipeline.generate_discrepancy_report(records, output_path=args.report)

    # Check for ground truth to score self-evaluation
    gt_path = Path(args.data) / "ground_truth.json"
    if gt_path.exists():
        print("\n[4/4] Evaluating against benchmark ground truth...")
        import json
        with open(gt_path, "r", encoding="utf-8") as f:
            truth = json.load(f)

        score_res = scoring.score_all(truth, submission)

        s1 = score_res["stage1"]
        s3 = score_res["stage3"]
        rel = score_res["reliability"]
        e2e = score_res["end_to_end"]

        print("\n" + "=" * 66)
        print("  BENCHMARK SCOREBOARD")
        print("=" * 66)
        print(f"  Stage 1 (Classification Macro-F1): {s1['macro_f1']:.4f} (Accuracy: {s1['accuracy']:.4f})")
        print(f"  Stage 3 (Defect Catch F1):         {s3['defect_f1']:.4f} (Exact Field Match: {s3['exact_match_rate']:.4f})")
        print(f"  Reliability (Escalation Recall):   {rel['escalation_recall']:.4f} (Precision: {rel['escalation_precision']:.4f})")
        print(f"  End-to-End Defect Catch Rate:      {e2e['rate']:.4f} ({e2e['success']}/{e2e['total']} defects)")
        print("-" * 66)
        print(f"  FINAL WEIGHTED SCORE:              {score_res['final_score']:.4f}")
        print("=" * 66)
    else:
        print("\n[4/4] No ground truth file found; submission ready for POST /submit.")

    print("\nPipeline execution complete.")


if __name__ == "__main__":
    main()
