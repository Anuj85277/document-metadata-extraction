import os
import pandas as pd
from src.pipeline import process_document

TEST_FOLDER = "data/test"
OUTPUT_FILE = "data/test_predictions.csv"

results = []

print("Starting batch prediction...\n")

for file_name in os.listdir(TEST_FOLDER):
    file_path = os.path.join(TEST_FOLDER, file_name)

    if not file_name.lower().endswith((".png", ".jpg", ".jpeg", ".docx")):
        continue

    print(f"Processing: {file_name}")

    try:
        prediction = process_document(file_path)
    except Exception as e:
        print(f"❌ Error processing {file_name}: {e}")
        prediction = {
            "Agreement Value": None,
            "Agreement Start Date": None,
            "Agreement End Date": None,
            "Renewal Notice (Days)": None,
            "Party One": None,
            "Party Two": None
        }

    prediction["file_name"] = file_name
    results.append(prediction)

df = pd.DataFrame(results)
df.to_csv(OUTPUT_FILE, index=False)

print("\n✅ Batch prediction completed successfully!")
print(f"📄 Output saved at: {OUTPUT_FILE}")
