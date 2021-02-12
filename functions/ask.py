from model.Question import Question
from data.data import ALL_LETTERS, ALL_QA, ALL_QUESTIONS, ALL_ANSWERS

def ask():
    print(f"--- Please answer the following questions ---")
    total_correct = 0
    total_correct_by_user = 0
    for idx, question in enumerate(ALL_QUESTIONS):
        answers = question.allAnswers
        print(f"\t{idx+1}) {question.textContent}")
        correctAnswers = []
        for idx, a in enumerate(answers):
            the_letter = ALL_LETTERS[idx]
            print(f"\t\t{the_letter}) {a['answer'].textContent}")
            if a['correctNess'] == True:
                correctAnswers.append(the_letter)

        user_raw_input = input()
        user_inputs = user_raw_input.split(',')
        print(f"You have chosen: {user_inputs}")

        num_correct = len(correctAnswers)
        num_correct_by_user = countHowManyCorrect(user_inputs, correctAnswers)
        print(f"Result: {num_correct_by_user}/{num_correct}")

        total_correct = total_correct + num_correct
        total_correct_by_user = total_correct_by_user + num_correct_by_user
    print(f"Final: {total_correct_by_user}/{total_correct}")


def countHowManyCorrect(user_inputs, listItems_to_match):
    counter = 0
    for listItem in listItems_to_match:
        num = [a for a in user_inputs if a == listItem]
        if len(num) > 0:
            counter = counter + 1
    return counter


