import random

def generate_mcqs(text, count=5):
    sentences = [s.strip() for s in text.split(".") if len(s.strip().split()) >= 4]
    questions = []

    for i in range(min(count, len(sentences))):
        sentence = sentences[i]
        words = sentence.split()
        correct_answer = words[-1].strip(".,")
        options = [correct_answer, "Option A", "Option B", "Option C"]
        random.shuffle(options)

        questions.append({
            "question": f"What is the missing word in: '{' '.join(words[:-1])} _____'?",
            "options": options,
            "answer": correct_answer
        })

    return questions

def generate_fillups(text, count=5):
    sentences = [s.strip() for s in text.split(".") if len(s.strip().split()) >= 5]
    questions = []

    for i in range(min(count, len(sentences))):
        words = sentences[i].split()
        blank_index = random.randint(1, len(words) - 2)
        answer = words[blank_index]
        words[blank_index] = "_____"

        questions.append({
            "question": " ".join(words),
            "answer": answer
        })

    return questions

def generate_true_false(text, count=5):
    sentences = [s.strip() for s in text.split(".") if len(s.strip().split()) >= 4]
    questions = []

    for i in range(min(count, len(sentences))):
        sentence = sentences[i]
        is_true = random.choice([True, False])
        modified = sentence

        if not is_true:
            modified = sentence.replace(" is ", " is not ").replace(" are ", " are not ")

        questions.append({
            "question": modified,
            "answer": "True" if is_true else "False"
        })

    return questions
