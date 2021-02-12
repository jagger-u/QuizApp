from colors import bcolors
import uuid

def generateID():
    return uuid.uuid1()

def trueFalseColored(input_bool):
    if input_bool:
        string = f"{bcolors.OKGREEN}({input_bool}){bcolors.ENDC}"
    else:
        string = f"{bcolors.FAIL}({input_bool}){bcolors.ENDC}"
    return string