from quizClass import QuestionAnswer, Question, Answer
from storage import ALL_LETTERS, ALL_QA, ALL_QUESTIONS, ALL_ANSWERS

def createQA(question, answer, correctNess):
    QA = QuestionAnswer(question.question_id, answer.answer_id, correctNess)
    ALL_QA.append(QA)
    return QA

def createQuestion(questionText):
    question = Question(questionText)
    ALL_QUESTIONS.append(question)
    return question

def createAnswer(answerText):
    answer = Answer(answerText)
    ALL_ANSWERS.append(answer)
    return answer