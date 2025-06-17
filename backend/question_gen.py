import re
import random

def generate_fill_in_blank_questions(text: str, count: int):
    sentences = re.split(r'(?<=[.?!])\s+', text.strip())
    sentences = [s for s in sentences if len(s.split()) > 5]

    questions = []
    used = set()

    for _ in range(count):
        if not sentences:
            break

        sentence = random.choice(sentences)
        words = sentence.split()
        keyword_candidates = [w for w in words if len(w) > 4 and w.isalpha()]
        if not keyword_candidates:
            continue

        keyword = random.choice(keyword_candidates)
        question_text = sentence.replace(keyword, "_____")
        if question_text in used:
            continue

        used.add(question_text)
        questions.append({
            "question": question_text,
            "answer": keyword
        })

    return questions


def generate_mcq_questions(text: str, count: int):
    sentences = re.split(r'(?<=[.?!])\s+', text.strip())
    sentences = [s for s in sentences if len(s.split()) > 5]

    questions = []
    for _ in range(count):
        if not sentences:
            break

        sentence = random.choice(sentences)
        words = [w for w in sentence.split() if len(w) > 4 and w.isalpha()]
        if len(words) < 4:
            continue

        correct_answer = random.choice(words)
        options = random.sample(words, min(4, len(words)))
        if correct_answer not in options:
            options[0] = correct_answer
        random.shuffle(options)

        questions.append({
            "question": f"What is the missing keyword in: \"{sentence.replace(correct_answer, '_____')}\"?",
            "options": options,
            "answer": correct_answer
        })

    return questions


def generate_true_false_questions(text: str, count: int):
    sentences = re.split(r'(?<=[.?!])\s+', text.strip())
    sentences = [s for s in sentences if len(s.split()) > 5]

    questions = []
    for i in range(min(count, len(sentences))):
        statement = sentences[i]
        # Optionally, we could flip some answers to False by altering them randomly
        questions.append({
            "question": statement,
            "answer": True
        })

    return questions


def generate_descriptive_questions(text: str, count: int):
    sentences = re.split(r'(?<=[.?!])\s+', text.strip())
    sentences = [s for s in sentences if len(s.split()) > 10]

    questions = []
    for i in range(min(count, len(sentences))):
        statement = sentences[i]
        questions.append({
            "question": f"Explain: {statement}",
            "answer": "User's descriptive answer here"
        })

    return questions


# Dispatcher
def generate_questions(text: str, question_type: str, count: int):
    if question_type in ["fill", "fillups"]:
        return generate_fill_in_blank_questions(text, count)
    elif question_type == "mcq":
        return generate_mcq_questions(text, count)
    elif question_type in ["tf", "truefa", "truefalse"]:
        return generate_true_false_questions(text, count)
    elif question_type == "descriptive":
        return generate_descriptive_questions(text, count)
    else:
        raise ValueError("Unsupported question type: " + question_type)
