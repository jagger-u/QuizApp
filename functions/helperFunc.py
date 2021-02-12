import uuid
from model.Terminal import Terminal

def generateID():
    return uuid.uuid1()

def trueFalseColored(input_bool):
    return Terminal.paintGreen(input_bool) if input_bool else Terminal.paintFail(input_bool)