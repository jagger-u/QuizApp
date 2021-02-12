from model.TerminalColor import TerminalColor
while True:
    print()
    welcome_msg = f'-----Write "quit" to exit.-----'
    exit_msg = f'-----Exitting-----'
    print(f'{TerminalColor.HEADER}{welcome_msg}{TerminalColor.ENDC}')
    user_input = input()
    if user_input == 'quit':
        print(f'{TerminalColor.FAIL}{exit_msg}{TerminalColor.ENDC}')
        break