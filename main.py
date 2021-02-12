from CRUD.create import createQuestion, createAnswer, createQA
from SHOW.display import displayAllQA, displayAllQuestions, displayAllAnswers, showAllQA
from storage import ALL_QUESTIONS
from EVAL.ask import ask, countHowManyCorrect
import pytest



"""
CREATE 
    - Questions and Answers
Description:
    - One question may have any number of:
        - incorrect answers
        - correct answers
    - One answer may be reused to be included in:
        - any number of questions
    - So there is a many to many relation
"""
# Questions
question_howManyDaysInYear = createQuestion("How many days are in a year?")
question_howManyDaysInWeek = createQuestion("How many days are in a week?")

# Answers
answer_300 = createAnswer("300")
answer_400 = createAnswer("400")
answer_365 = createAnswer("365")
answer_7 = createAnswer("7")
answer_100 = createAnswer("100")
answer_not8 = createAnswer("Not 8")
answer_seven = createAnswer("Seven")

# QA for question_howManyDaysInYear
createQA(question_howManyDaysInYear, answer_300, False)
createQA(question_howManyDaysInYear, answer_400, False)
createQA(question_howManyDaysInYear, answer_365, True)
createQA(question_howManyDaysInYear, answer_7, False)

# QA for question_howManyDaysInWeek
createQA(question_howManyDaysInWeek, answer_7, True)
createQA(question_howManyDaysInWeek, answer_not8, True)
createQA(question_howManyDaysInWeek, answer_seven, True)
createQA(question_howManyDaysInWeek, answer_400, False)
createQA(question_howManyDaysInWeek, answer_100, False)


"""
DISPLAY
    - All questions and the answers of each
"""
print("")
displayAllQA()
print("")
displayAllQuestions()
print("")
displayAllAnswers()

print("")
showAllQA()

"""
STDIN
    Now we will ask and correct it
"""
print("")
ask()

