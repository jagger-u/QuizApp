from functions.helperFunc import generateID, trueFalseColored
from data.data import ALL_LETTERS, ALL_QA, ALL_QUESTIONS, ALL_ANSWERS

class Answer:
    def __init__(self, textContent):
        self.answer_id = generateID()
        self.textContent = textContent

    @classmethod
    def insertAnswer(cls, answerText):
        answer = cls(answerText)
        ALL_ANSWERS.append(answer)
        return answer

    @staticmethod
    def getAnswerById(answer_id):
        return [a for a in ALL_ANSWERS if a.answer_id == answer_id][0]

    @staticmethod
    def displayAllAnswers(): 
        print(f"--- List of Answers ---")   
        for idx, answer in enumerate(ALL_ANSWERS):
            print(f"\t{idx+1}) {answer.textContent}")