from functions.helperFunc import generateID
from data.data import ALL_LETTERS, ALL_QA, ALL_QUESTIONS, ALL_ANSWERS

class QA:
    def __init__(self, question_id, answer_id, correctNess):
        self.qa_id = generateID()
        self.question_id = question_id
        self.answer_id = answer_id 
        self.correctNess = correctNess # boolean

    @classmethod
    def insertQA(cls, question, answer, correctNess):
        QA = cls(question.question_id, answer.answer_id, correctNess)
        ALL_QA.append(QA)
        return QA

    @staticmethod
    def getQAById(qa_id):
        return [qa for qa in ALL_QA if qa.qa_id == qa_id][0]

    @staticmethod
    def displayAllQA():
        print(f"--- List of QA ---")
        for idx, qa in enumerate(ALL_QA):
            question = [q for q in ALL_QUESTIONS if q.question_id == qa.question_id][0]
            answer = [a for a in ALL_ANSWERS if a.answer_id == qa.answer_id][0]
            print(f"\t{idx+1}) \"{question.textContent}\" {answer.textContent}")

    # TODO: need to use "find" instead of filter, how to guarantee only one will be there?
    def showAllQA():
        print(f"--- Showing QA ---")
        for idx, question in enumerate(ALL_QUESTIONS):
            print(f'\t{idx+1}) {question.textContent}')
            question.displayAnswers()