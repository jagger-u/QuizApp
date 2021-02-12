from helperFunc import generateID
from storage import ALL_LETTERS, ALL_QA, ALL_QUESTIONS, ALL_ANSWERS
from helperFunc import trueFalseColored
    
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










