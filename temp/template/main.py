import subprocess
import os

SYNTAX = {
    "create": ["create", "c"],
    "use": ["use", "u"]
}

# check if template file exist
FILENAME = "template.txt"
PATH = os.path.dirname(os.path.abspath(__file__))
FILEPATH = f"{PATH}\{FILENAME}"
open(FILEPATH, 'a').close()

class Template: 
    def __init__(self, *args):
        # If no parameter are passed, show help message
        if not args[0]: 
            self.helpMessage()
            return
        
        if args[0][0] in SYNTAX["create"]: 
            self.crate()
            return

        if args[0][0] in SYNTAX["use"]: 
            self.use()
            return

        print(os.getcwd())
        print("Test: __init__")
        print(f"Command arguments: {args[0]}")

    def errorMessage(self):
        print('''
incorrect command syntax
type help for comnands list
    ''')

    def helpMessage(self):
        print('''
use of template:
    - create [name] [url]
    - use [name] 
    ''')    

    def crate(self):
        print("create")

    def use(self):
        p = os.system("cd .>test.txt")
        print("use")
    