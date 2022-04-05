# Sau-CLI
Main sau cli application

### How to use
###### To call a command directly from console:
```
python .\sau.py [command] [syntax]
```

###### To call a command with auto syntax:
```
python .\sau.py
```
It will open a python script with an input
```
(auto) sau: [command] [syntax]
```
it automatically read the syntax of the comnands and create an autocompile that can be use usin tab

###### To compile
```
compile.bat
```
*ATTENTION:* pyinstaller have to be present as global command to compile.
The compiler will create a sau.exe in _dist_ folder. All the _src_ file will be copied to the new location, except for all the files with extection marked in exclude.bat.txt. In that case the old version of the file will be keeped (will not be overwrite)

### To do
 - [X] Dynamic module import
 - [X] Dynamic syntax autocomplete
 - [X] Dynamic module function call
 - [ ] Automatically description on help
 - [ ] Automatically description on error
 - [ ] Create new package command
 - [ ] Set sau.exe as enviroment variable
 - [ ] ...


### How to create a new module
See at demo for basic module example
1) Under _src_ create a new folder with the module name
2) Create a ```__init__.py ``` and a ``` main.py ``` file in the folder, as well a ``` syntax.json ```.
3) In ``` syntax.json ``` create a structure like this one:
```json
{
    "demo": {
        "desc": "this is a demo description",
        "sub": {
            "command1": {
                "description": "command1",
                "sub": {
                    "sub_demo1": {
                        "call": "sub_demo1"
                    },
                    "sub_demo2": {
                        "call": "sub_demo2"
                    }
                }
            }
        }
    }
}
```
4) Inside ``` main.py ``` create a class
```python
class Demo:
    def __init__(self, *args) -> None:
        print("This get called every time an user put the command Demo")
    
    def sub_demo1(self):
        print("You have called sub_demo1")
    
    def sub_demo2(self):
        print("You have called sub_demo2")
```
the function named in "call" in the json file will be called if the command with the entire syntax has been called. 

5) Finally inside ```__init__.py ``` has to be exported the Demo class:
```python
from src.demo.main import Demo
```

try the command from the console and with the autocomplete so check the functionality. 