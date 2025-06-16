from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from utils.file_utils import extract_text_from_file
from question_gen import generate_mcqs, generate_fillups, generate_true_false

app = FastAPI()

# Allow frontend connections
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Backend is alive"}

@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    question_type: str = Form(...),
    question_count: int = Form(...)
    
):
    
    try:
        text = await extract_text_from_file(file)
    except Exception as e:
        return {"error": f"Failed to extract text: {str(e)}"}

    if not text.strip():
        return {"error": "No readable text found in file"}

    if question_type == "mcq":
        questions = generate_mcqs(text, question_count)
    elif question_type == "fillups":
        questions = generate_fillups(text, question_count)
    elif question_type == "truefalse":
        questions = generate_true_false(text, question_count)
    else:
        return {"error": "Invalid question type"}

    return {
        "filename": file.filename,
        "text_preview": text[:300],
        "questions": questions
    }
