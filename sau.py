# Import libs
import sys # instead of exit() use sys.exit()
import os
import json
from prompt_toolkit import prompt
from prompt_toolkit.completion import NestedCompleter

# Import commands script 
import src
import src.util as util

# GLobal constants
DEVELOP = True

class Sau:
    def __init__(self):
        # Check if users haven't pass paramterts -> ho in autocomplete mode
        if len(sys.argv) < 2: 
            self.loadAutoComplete()
            self.autoComplete()
        
        # parse command
        else:
            self.command = sys.argv[1:][0].lower()
            self.args = sys.argv[2:]
            self.text = " ".join(sys.argv[1:])
        
        self.callCommand()

    # Load all the autocompile syntax from module  
    def loadAutoComplete(self):
        modules = util.getModules()
        syntax = {}
        for module in modules:
            sy = util.getSyntax(f"./src/{module}")
            syntax.update(sy)
        self.COMPLETER = NestedCompleter.from_nested_dict(syntax)

    def autoComplete(self):
        self.text = prompt('(auto) sau ', completer=self.COMPLETER)
        self.command = self.text.split(" ")[0]
        self.args = self.text.split(" ")[1:]
    
    def callCommand(self):
        try:
            print(self.args)
            print(self.command)
            print(self.text)
            execute = util.getFunction(self.text)
            if not execute and execute != {}:
                print("command not found")
                return
            klass = getattr(src, self.command.title())
            comm = klass(self.args)
            if (self.args != []):
                func = getattr(klass, execute)
                func(comm)

        except ValueError as e:
            if DEVELOP: print(e)

Sau()