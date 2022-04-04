# Import sys args
from distutils.log import error
import sys

DEVELOP = True
# Define functions
def displayhelp():
    print("help")

# check if user type just sau display help
if len(sys.argv) < 2: 
    displayhelp()
    sys.exit()

command = sys.argv[1:][0]
command = command.lower()
args = sys.argv[2:]

help = ["help", "h"]
if command in help:
    displayhelp()
    sys.exit()

# Import commands script 
import src

# Try to call comand
try:
    klass = getattr(src, command.title())
    some_object = klass(args)

except error as e:
    if DEVELOP: print(e)
    print('''
incorrect command syntax
type help for comnands list
    ''')