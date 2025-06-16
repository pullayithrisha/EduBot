def generate_questions(text, question_type, count):
    dummy_questions = []

    for i in range(count):
        if question_type == "mcq":
            dummy_questions.append({
                "question": f"MCQ Question {i+1} from content.",
                "options": ["Option A", "Option B", "Option C", "Option D"],
                "answer": "Option A"
            })
        elif question_type == "fillups":
            dummy_questions.append({
                "question": f"Fill in the blank {i+1} from content.",
                "answer": "ExampleAnswer"
            })
        elif question_type == "truefalse":
            dummy_questions.append({
                "question": f"True/False Question {i+1} from content.",
                "answer": True
            })
        elif question_type == "descriptive":
            dummy_questions.append({
                "question": f"Descriptive Question {i+1} from content.",
                "answer": "Sample descriptive answer."
            })

    return dummy_questions
