import pandas as pd
import re
from dateutil import parser

COLUMN_MAP = {
    "Aggrement Value": "Agreement Value",
    "Aggrement Start Date": "Agreement Start Date",
    "Aggrement End Date": "Agreement End Date",
    "Renewal Notice (Days)": "Renewal Notice (Days)",
    "Party One": "Party One",
    "Party Two": "Party Two",
}


def normalize_value(val):
    if pd.isna(val) or str(val).strip() == "":
        return None

    val = str(val).lower().strip()

    # normalize currency
    val = re.sub(r"(rs\.?|₹|inr)", "", val)
    val = re.sub(r"[,\s]", "", val)

    # normalize dates
    try:
        parsed = parser.parse(val, dayfirst=True)
        return parsed.strftime("%Y-%m-%d")
    except Exception:
        pass

    # normalize text
    val = re.sub(r"\s+", " ", val)
    return val


def compute_recall(gt_path, pred_path):
    gt = pd.read_csv(gt_path)
    pred = pd.read_csv(pred_path)

    # align row-wise
    n = min(len(gt), len(pred))
    gt = gt.iloc[:n]
    pred = pred.iloc[:n]

    results = {}

    for gt_col, pred_col in COLUMN_MAP.items():
        true_count = 0
        false_count = 0

        for i in range(n):
            gt_val = normalize_value(gt.iloc[i][gt_col])
            pred_val = normalize_value(pred.iloc[i][pred_col])

            if gt_val == pred_val and gt_val is not None:
                true_count += 1
            else:
                false_count += 1

        recall = true_count / (true_count + false_count) if (true_count + false_count) else 0
        results[pred_col] = round(recall, 3)

    return results


if __name__ == "__main__":
    scores = compute_recall(
        "data/test.csv",
        "data/test_predictions.csv"
    )

    print("\n📊 Per-Field Recall Scores:\n")
    for field, score in scores.items():
        print(f"{field}: {score}")
