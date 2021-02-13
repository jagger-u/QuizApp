from model.QA import QA
from model.Question import Question
from model.Answer import Answer
from data.data import ALL_QUESTIONS
from functions.ask import ask, countHowManyCorrect
from model.Terminal import Terminal

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
print(Terminal.paintHeader(Terminal.writeHeader('Welcome to the Quiz!')))
print('Options:')
print('\t- To create a quiz, write "create"')
print('\t- To give a quiz, write "go"')
print('\t- To exit, write "quit"')
while True:
    user_input = input("[Mainloop] Enter option: ")
    if user_input == 'quit':
        print(Terminal.paintFooter(Terminal.writeFooter("[Mainloop] Leaving...")))
        break
    elif user_input == 'create':
        all_answers = []

        print(Terminal.paintBlue("[Step 1]: Create a question"))
        user_input = input("Enter the question: ")
        new_question = user_input

        print(Terminal.paintBlue(f'[Step 2]: Create the answer(s) for "{new_question}"'))

        while True:
            user_input = input("Enter the answer: ")
            if user_input == 'quit':
                print("Leaving 'create'")
                break
            new_answer = user_input
            



            while True:
                user_input = input("Is it a correct answer to that question? [y/n]: ")                
                if user_input == 'y':
                    all_answers.append({"answer": new_answer, "correctNess": True})
                    break
                elif user_input  == 'n':
                    all_answers.append({"answer": new_answer, "correctNess": False})
                    break
                elif user_input == 'quit':
                    print("Leaving correct answer or not")
                    break
                else:
                    print(Terminal.paintFail("Invalid input, please enter [y/n] or write [quit] to exit."))


            while True:
                user_input = input("Add another? [y/n]: ")
                if user_input == 'n':
                    user_input = 'quit'
                    break
                elif user_input == 'y':
                    break
                else:
                    print(Terminal.paintFail("Invalid input, please enter [y/n] or write [quit] to exit."))
            if user_input == 'quit':
                break

        print(Terminal.paintGreen("Saving..."))
        # TODO: need to save changes, update the models etc...
        # TODO: need to create a truth table sort of thing, map out all the possibilities   ...
        # TODO: need to run tests! Write all the test cases...
        print(f'\t {new_question}')
        for item in all_answers:
            print(f'\t\t- {item["answer"]} ({item["correctNess"]})')
        print(Terminal.paintGreen("Saved."))




    elif user_input == 'go':
        print(Terminal.paintBlue("Starting quiz..."))
        ask()
    else:
        print(Terminal.paintFail("Invalid input, try again..."))

