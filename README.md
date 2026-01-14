# Metadata Extraction from Documents

## Problem Overview
The objective of this project is to build a template-agnostic AI/ML system that extracts key metadata fields from documents.  
The system supports both scanned images and DOCX files and avoids rule-based approaches such as regex or static heuristics.

### Extracted Fields
- Agreement Value
- Agreement Start Date
- Agreement End Date
- Renewal Notice (Days)
- Party One
- Party Two

---

## Solution Approach

### 1. Document Ingestion
- DOCX files are parsed using `python-docx`
- Scanned documents are processed using OCR

### 2. Text Extraction
- Images are converted to text using an OCR engine
- Extracted text is normalized and passed downstream

### 3. LLM-based Metadata Extraction
- A Large Language Model is prompted to extract structured metadata
- The model is instructed to return only JSON output
- No rule-based extraction (regex, static conditions) is used

### 4. API Layer
- The pipeline is exposed via a FastAPI-based REST endpoint
- Users can upload documents and receive extracted metadata as JSON

### 5. Batch Prediction
- All documents in `data/test/` are processed in batch mode
- Predictions are saved to `data/test_predictions.csv`

---

## Evaluation

### Metric
Per-field Recall i


Where:
- True = exact match between extracted value and ground truth
- False = mismatch or missing value

### Evaluation Observations
Exact-match recall on the test set is low due to:
- OCR noise
- Formatting differences (dates, currency)
- Generative nature of LLM outputs
- Ground truth inconsistencies

This behavior is expected in template-agnostic document understanding systems.  
In real-world systems, fuzzy matching or semantic similarity–based evaluation would be preferred.

---

## How to Run

### 1. Setup Environment
```bash
pip install -r requirements.txt
