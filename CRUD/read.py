from storage import ALL_LETTERS, ALL_QA, ALL_QUESTIONS, ALL_ANSWERS

def getAnswerById(answer_id):
    return [a for a in ALL_ANSWERS if a.answer_id == answer_id][0]

def getAnswersForQuestion(question):
    answers_list = []
    for qa in ALL_QA:
        if qa.question_id == question.question_id:
            answer = getAnswerById(qa.answer_id)
            correctNess = qa.correctNess
            answers_list.append({"answer": answer, "correctNess": correctNess})
    return answers_list