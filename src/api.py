from fastapi import FastAPI, UploadFile, File
import shutil, uuid
from src.pipeline import process_document

app = FastAPI()

@app.post("/extract-metadata")
async def extract_metadata_api(file: UploadFile = File(...)):
    file_path = f"temp_{uuid.uuid4()}_{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = process_document(file_path)
    return result
