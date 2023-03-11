import json
import os

def pPrint(value: dict):
    print(json.dumps(value, indent=4, sort_keys=True))

def getModules():
    modules = [name for name in os.listdir("./src") if os.path.isdir(os.path.join("./src", name))]
    if "__pycache__" in modules: modules.remove("__pycache__")
    if "util" in modules: modules.remove("util")
    excude = []
    with open("./src/exclude.module.txt","r") as file:
        excude = file.read().split("\n")
    for module in excude:
        if module in modules: modules.remove(module)
    return modules

def getSyntax(_file):
    def returnSubCommands(_tree: dict):
        key = [i for i in _tree.keys()][0]
        dic =  {key: {}}
        if "sub" in _tree[key]:
            for i in _tree[key]["sub"]:
                dic[key].update(returnSubCommands({i: _tree[key]["sub"][i]}))
            return dic
        else:
            return {key: None}

    with open(_file+"/syntax.json","r") as file:
        f = json.loads(file.read())
        name = [i for i in f.keys()][0]
        syntax = {name: {}}
        syntax.update(returnSubCommands(f))
        return syntax

def getFunction(text):
    commands = text.split(" ")
    path = f"./src/{commands[0]}/syntax.json"
    # Check if path don't exist
    if (not os.path.isfile(path)):
        return None
    # Check if exist but root command
    if (os.path.isfile(path) and len(commands) == 1):
        return {}
    with open(path,"r") as file:
        syntax = json.loads(file.read())
        for command in commands:
            if command in syntax: 
                if "sub" in syntax[command]: syntax = syntax[command]["sub"]
                elif "call" in syntax[command]: return syntax[command]["call"]
                else: return None
    return None

def getPath(_path):
    return os.path.dirname(os.path.abspath(_path))