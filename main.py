from quizClass import QA, Question, Answer
from storage import ALL_QUESTIONS
from ask import ask, countHowManyCorrect


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
question_howManyDaysInYear = Question.insertQuestion("How many days are in a year?")
question_howManyDaysInWeek = Question.insertQuestion("How many days are in a week?")

# Answers
answer_300 = Answer.insertAnswer("300")
answer_400 = Answer.insertAnswer("400")
answer_365 = Answer.insertAnswer("365")
answer_7 = Answer.insertAnswer("7")
answer_100 = Answer.insertAnswer("100")
answer_not8 = Answer.insertAnswer("Not 8")
answer_seven = Answer.insertAnswer("Seven")

# QA for question_howManyDaysInYear
QA.insertQA(question_howManyDaysInYear, answer_300, False)
QA.insertQA(question_howManyDaysInYear, answer_400, False)
QA.insertQA(question_howManyDaysInYear, answer_365, True)
QA.insertQA(question_howManyDaysInYear, answer_7, False)

# QA for question_howManyDaysInWeek
QA.insertQA(question_howManyDaysInWeek, answer_7, True)
QA.insertQA(question_howManyDaysInWeek, answer_not8, True)
QA.insertQA(question_howManyDaysInWeek, answer_seven, True)
QA.insertQA(question_howManyDaysInWeek, answer_400, False)
QA.insertQA(question_howManyDaysInWeek, answer_100, False)


"""
DISPLAY
    - All questions and the answers of each
"""
print("")
QA.displayAllQA()
print("")
Question.displayAllQuestions()
print("")
Answer.displayAllAnswers()

print("")
QA.showAllQA()

"""
STDIN
    Now we will ask and correct it
"""
print("")
ask()

