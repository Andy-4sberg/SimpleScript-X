# **Developer Note:**
### Please don't edit directly, use code like this:
``` python 3
from main import *
while executing:
    code = input(colored('> ','red'))
    text = code.split()
    try:
        if text[0] == "custom": print('This is an external command')
        # text[0] is the first word in the command
        
        elif text[0] == "clear": print('This is overwriting the \'clear\' command')
        # You can overwrite commands that already exist

        else: SimpleScriptX(text,code)
        # If the command isn't here, check SimpleScript X for it

    except: print("ERROR")
```
--------------------------
## getval()
--------------------------
#### **Syntax:**
``` python 3
getval(varName)
```
#### Returns value of SimpleScript X variable
--------------------------
## proccess_math()
--------------------------
#### **Syntax:**
```
text = '50 * 100'
proccess_math(text, text.split())
```
#### Returns value of math operation
--------------------------
## run_logic()
--------------------------
#### **Syntax:**
```
run_logic(10,'==',10)
```
#### Returns bool (True/False for ==, =!, etc.)
--------------------------
## SimpleScriptX()
--------------------------
#### **Syntax:**
```
command = 'help'
SimpleScriptX(command, command.split())
```
#### Returns output of command
--------------------------
## run_file()
--------------------------
#### **Syntax:**
``` python 3
run_file(fileName)
```
#### Executes SimpleScript X file
--------------------------
###### **Please read LICENSE**