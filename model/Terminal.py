"""
    Source: stackoverflow.com
    Description: colors for the terminal
    Link: https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal
"""
class Terminal:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m' 
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @classmethod
    def paintHeader(cls, input_text):
        return f"{cls.HEADER}{input_text}{cls.ENDC}"

    @classmethod
    def paintBlue(cls, input_text):
        return f"{cls.OKBLUE}{input_text}{cls.ENDC}"

    @classmethod
    def paintGreen(cls, input_text):
        return f"{cls.OKGREEN}{input_text}{cls.ENDC}"

    @classmethod
    def paintFail(cls, input_text):
        return f"{cls.FAIL}{input_text}{cls.ENDC}"

    @classmethod
    def paintFooter(cls, input_text):
        return f"{cls.FAIL}{input_text}{cls.ENDC}"

    @classmethod
    def paintSummary(cls, input_text):
        return f"{cls.BOLD}{cls.OKCYAN}{input_text}{cls.ENDC}"
        
    @classmethod
    def writeHeader(cls, input_text):
        return f"\n-----{input_text}-----\n"

    @classmethod
    def writeFooter(cls, input_text):
        return f"\n-----{input_text}-----\n"
