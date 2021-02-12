from helperFunc import generateID
class QuestionAnswer:
    def __init__(self, question_id, answer_id, correctNess):
        self.questionAnswerd_id = generateID()
        self.question_id = question_id
        self.answer_id = answer_id 
        self.correctNess = correctNess # boolean

class Question:
    def __init__(self, textContent, difficulty='medium', max_trials='2'):
        self.question_id = generateID()
        self.textContent = textContent
        self.difficulty = difficulty
        self.max_trials = max_trials

class Answer:
    def __init__(self, textContent):
        self.answer_id = generateID()
        self.textContent = textContent