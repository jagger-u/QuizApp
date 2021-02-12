from functions.helperFunc import generateID, trueFalseColored
from data.data import ALL_LETTERS, ALL_QA, ALL_QUESTIONS, ALL_ANSWERS
from model.Answer import Answer

class Question:
    def __init__(self, textContent, difficulty='medium', max_trials='2'):
        self.question_id = generateID()
        self.textContent = textContent
        self.difficulty = difficulty
        self.max_trials = max_trials

    @classmethod
    def insertQuestion(cls, questionText):
        question = cls(questionText)
        ALL_QUESTIONS.append(question)
        return question

    @staticmethod
    def getQuestionById(question_id):
        return [q for q in ALL_QA if q.question_id == question_id][0]

    @property
    def allAnswers(self):
        labelled_answers = []
        for qa in ALL_QA:
            if qa.question_id == self.question_id:
                answer = Answer.getAnswerById(qa.answer_id)
                correctNess = qa.correctNess
                labelled_answers.append({"answer": answer, "correctNess": correctNess})
        return labelled_answers

    # TODO: raise exception if the number of answers is greater than available letters
    def displayAnswers(self):
        answers = self.allAnswers
        for idx, a in enumerate(answers):
            print(f'\t\t{ALL_LETTERS[idx]}) {a["answer"].textContent} {trueFalseColored(a["correctNess"])}')

    @staticmethod
    def displayAllQuestions(): 
        print(f"--- List of Questions ---")   
        for idx, question in enumerate(ALL_QUESTIONS):
            print(f"\t{idx+1}) {question.textContent}")
