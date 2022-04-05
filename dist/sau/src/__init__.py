import os

# Import all util function from util.py
from .util import *

# dynamically rappresentation of ---> from src.demo.[name] import *
def importModule(name: str):
    module = __import__(f"src.{name}", fromlist=['*'])

    if hasattr(module, '__all__'):
        all_names = module.__all__
    else:
        all_names = [name for name in dir(module) if not name.startswith('_')]

    globals().update({name: getattr(module, name) for name in all_names})


# Load all modules
modules = [name for name in os.listdir(__path__[0]) if os.path.isdir(os.path.join(__path__[0], name))]
if "__pycache__" in modules: modules.remove("__pycache__")

# List of module to be excluded
excude = []
with open(f"{__path__[0]}/exclude.module.txt","r") as file:
    excude = file.read().split("\n")
for module in excude:
    if module in modules: modules.remove(module)
for module in modules: importModule(module)