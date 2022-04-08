from importlib.resources import path
import src.util as util
import os

MPATH = util.getPath(__file__)
PATH = os.getcwd()

class Module:
    def __init__(self, *args) -> None:
        pass

    def createBlank(self):
        print()
        print("You have called sub_demo1")
    