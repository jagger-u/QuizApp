from CRUD.read import getAnswersForQuestion
from storage import ALL_LETTERS, ALL_QA, ALL_QUESTIONS, ALL_ANSWERS
from helperFunc import trueFalseColored
    
# TODO: raise exception if the number of answers is greater than available letters
def displayAnswersForQuestion(question):
    answers = getAnswersForQuestion(question)
    for idx, a in enumerate(answers):
        print(f'\t\t{ALL_LETTERS[idx]}) {a["answer"].textContent} {trueFalseColored(a["correctNess"])}')

def displayAllQA():
    print(f"--- List of QA ---")
    for idx, qa in enumerate(ALL_QA):
        question = [q for q in ALL_QUESTIONS if q.question_id == qa.question_id][0]
        answer = [a for a in ALL_ANSWERS if a.answer_id == qa.answer_id][0]
        print(f"\t{idx+1}) \"{question.textContent}\" {answer.textContent}")


def displayAllQuestions(): 
    print(f"--- List of Questions ---")   
    for idx, question in enumerate(ALL_QUESTIONS):
        print(f"\t{idx+1}) {question.textContent}")

def displayAllAnswers(): 
    print(f"--- List of Answers ---")   
    for idx, answer in enumerate(ALL_ANSWERS):
        print(f"\t{idx+1}) {answer.textContent}")

# TODO: need to use "find" instead of filter, how to guarantee only one will be there?
def showAllQA():
    print(f"--- Showing QA ---")
    for idx, question in enumerate(ALL_QUESTIONS):
        print(f'\t{idx+1}) {question.textContent}')
        displayAnswersForQuestion(question)