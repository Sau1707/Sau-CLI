import subprocess
import os
import src.util as util

PATH = util.getPath(__file__)
SYNTAX = util.getSyntax(PATH)

# check if template file exist
FILENAME = "template.txt"
FILEPATH = f"{PATH}\{FILENAME}"
open(FILEPATH, 'a').close()

class Template: 
    def __init__(self, *args):
        return

    def crate(self):
        print("create")

    def use(self):
        print("use")
    