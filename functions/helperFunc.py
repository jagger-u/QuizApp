import uuid
from model.TerminalColor import TerminalColor

def generateID():
    return uuid.uuid1()

def trueFalseColored(input_bool):
    if input_bool:
        string = f"{TerminalColor.OKGREEN}({input_bool}){TerminalColor.ENDC}"
    else:
        string = f"{TerminalColor.FAIL}({input_bool}){TerminalColor.ENDC}"
    return string