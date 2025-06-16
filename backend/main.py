from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from utils.file_utils import extract_text_from_file
from question_gen import generate_questions
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Backend is running."}

@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    question_type: str = Form(...),
    question_count: int = Form(...)
):
    contents = await file.read()
    filename = file.filename

    temp_dir = "temp_files"
    os.makedirs(temp_dir, exist_ok=True)
    temp_path = os.path.join(temp_dir, filename)

    with open(temp_path, "wb") as f:
        f.write(contents)

    extracted_text = extract_text_from_file(temp_path)
    questions = generate_questions(extracted_text, question_type, int(question_count))

    return {
        "text_preview": extracted_text[:500],
        "questions": questions
    }
