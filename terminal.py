from model.Terminal import Terminal
print(Terminal.paintHeader(Terminal.writeHeader('Welcome to the Quiz!')))
print('Options:')
print('\t- To give a quiz, write "go"')
print('\t- To exit, write "quit"')
while True:
    user_input = input("Enter option: ")
    if user_input == 'quit':
        print(Terminal.paintFooter(Terminal.writeFooter('Exitting')))
        break
    elif user_input == 'go':
        print(Terminal.paintBlue("Starting quiz..."))
    else:
        print(Terminal.paintFail("Invalid input, try again..."))