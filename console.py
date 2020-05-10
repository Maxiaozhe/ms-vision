from enum import Enum
from colorama import init, Fore
class Level(Enum):
    INFO=0
    WARNING = 1
    ERROR = 2
    
def log(message, level=Level.INFO):
    if level==Level.ERROR:
        print(Fore.RED, message)
    elif level == Level.WARNING:
        print(Fore.YELLOW, message)
    elif level == Level.INFO:
        print(Fore.GREEN, message)
    else:
        print(message)
    init()

