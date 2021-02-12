from model.Question import Question
from model.Terminal import Terminal
from data.data import ALL_LETTERS, ALL_QA, ALL_QUESTIONS, ALL_ANSWERS
import time
max_trials = 10

def ask():
    print(Terminal.paintHeader("Please answer the following questions"))

    total_correct = 0
    total_correct_by_user = 0

    user_raw_input = None

    for i, question in enumerate(ALL_QUESTIONS):
        trials = 0
        time.sleep(1)
        while True:
            print(f"\t{i+1}) {question.textContent} {max_trials - trials} trials left. Score: {total_correct_by_user}")
            correctAnswers = []

            answers = question.allAnswers
            for idx, a in enumerate(answers):
                the_letter = ALL_LETTERS[idx]
                print(f"\t\t{the_letter}) {a['answer'].textContent}")
                if a['correctNess'] == True:
                    correctAnswers.append(the_letter)
            user_raw_input = input("[AskLoop:] Enter answer: ")
            user_inputs = user_raw_input.split(',')
            if user_raw_input == 'quit':
                print("leaving while loop in ask()...")
                break
            num_correct = len(correctAnswers)
            num_correct_by_user = countHowManyCorrect(user_inputs, correctAnswers)

            print(f"You have chosen: {user_inputs}")

            allCorrect = num_correct_by_user == num_correct
            feedbackMsg = f'{Terminal.paintFail("INCORRECT!")} Your result is: '
            if allCorrect:
                feedbackMsg = f'{Terminal.paintGreen("CORRECT!")} Your result is: '
                
            print(f"{feedbackMsg}{num_correct_by_user}/{num_correct}")

            if allCorrect or trials == max_trials:
                total_correct += num_correct
                total_correct_by_user += num_correct_by_user
                break
            else:
                trials += 1
        if user_raw_input == 'quit':
            print("leaving for loop in ask()...")
            break
    print(f"Final: {total_correct_by_user}/{total_correct}")
    return user_raw_input




def countHowManyCorrect(user_inputs, listItems_to_match):
    counter = 0
    for listItem in listItems_to_match:
        num = [a for a in user_inputs if a == listItem]
        if len(num) > 0:
            counter = counter + 1
    return counter


