from colors import bcolors
while True:
    print()
    welcome_msg = f'-----Write "quit" to exit.-----'
    exit_msg = f'-----Exitting-----'
    print(f'{bcolors.HEADER}{welcome_msg}{bcolors.ENDC}')
    user_input = input()
    if user_input == 'quit':
        print(f'{bcolors.FAIL}{exit_msg}{bcolors.ENDC}')
        break