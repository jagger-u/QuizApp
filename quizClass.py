from helperFunc import generateID
from storage import ALL_LETTERS, ALL_QA, ALL_QUESTIONS, ALL_ANSWERS
class QA:
    def __init__(self, question_id, answer_id, correctNess):
        self.qa_id = generateID()
        self.question_id = question_id
        self.answer_id = answer_id 
        self.correctNess = correctNess # boolean

    @classmethod
    def createQA(cls, question, answer, correctNess):
        QA = cls(question.question_id, answer.answer_id, correctNess)
        ALL_QA.append(QA)
        return QA

class Question:
    def __init__(self, textContent, difficulty='medium', max_trials='2'):
        self.question_id = generateID()
        self.textContent = textContent
        self.difficulty = difficulty
        self.max_trials = max_trials

    @classmethod
    def createQuestion(cls, questionText):
        question = cls(questionText)
        ALL_QUESTIONS.append(question)
        return question



class Answer:
    def __init__(self, textContent):
        self.answer_id = generateID()
        self.textContent = textContent

    @classmethod
    def createAnswer(cls, answerText):
        answer = cls(answerText)
        ALL_ANSWERS.append(answer)
        return answer



