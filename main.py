"""

"""
# Setup
import os, sys
from sys import *
from termcolor import colored, cprint

os.system('clear')

variables = {}  # Variable that stores variables
functions = {}

version = [1.0, "beta"]  # Variable storing the version
executing = True  # Is SimpleScript X running?
DEFINING_FUNCTION = False
shell = "> "  # Shell message for each line
#lexer, might work on parsing in a little
math = ["+", "-", "*", "/", "%"]

global compiled

""""
class BasicLexer(Lexer):
    tokens = {NAME, NUMBER, STRING}
    ignore = '/t'
    literals = {'=', '+', '-', '/', '*', '(', ')', ',', ';'}
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    STRING = r'\".*?\"'

    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    @_(r'//.*')
    def COMMENT(self, t):
        pass
"""
ln = 0
sys_color = "blue"
functionName = ""
cprint(
    f"SimpleScript X v{version[0]} ({version[1]})\n\nType \"help\" for a list of commands\n\n",
    sys_color,
    attrs=['bold'])  # Displays version on startup
commands = {
    "help           ": "Shows all available commands",
    "print          ": "Prints text to the screen",
    "print $        ": "Prints value of a variable",
    "printx         ": "prints colored text to the screen",
    "var            ": "Creates a variable",
    "var list       ": "Creates a list",
    "*              ": "Creates a comment",
    "prompt         ": "Asks for user input",
    "exit           ": "Exits SimpleScript X",
    "clear          ": "Clears the screen",
    "write x to file": "Writes x to file"
}

def getval(var):
    if var[0] == "$":
        try:
          return float(variables[var[1:].replace(" ","")])
        except ValueError:
          return variables[var[1:]]
        except TypeError:
          return variables[var[1:]]
    else:
        try: 
          return float(var.replace(" ",""))
        except ValueError:
          return var
        except TypeError:
          return var

def process_math(text, full):
    try:
      global code
      full = full.split('=', 1)[-1]
        
      if '+' in text:
        a = full.split('+', 1)[0]
        if ',' in a: a.split(',')
        a = getval(a.replace(" ",""))

        b = full.split('+', 1)[-1]
        if ',' in b: b.split(',')
        b = getval(b.replace(" ",""))

        return(a+b)

      elif '-' in text:
        a = full.split('-', 1)[0]
        if ',' in a: a.split(',')
        a = getval(a.replace(" ",""))
        b = full.split('-', 1)[-1]
        if ',' in b: b.split(',')
        b = getval(b.replace(" ",""))

        return(a-b)

      elif text[1] == '*':
        a = getval(text[0])
        b = getval(text[2])

        return(a*b)
      elif text[1] == '/':
        a = getval(text[0])
        b = getval(text[2])

        return(a/b)

      elif text[1] == '%':
        a = getval(text[0])
        b = getval(text[2])

        return(a % b)
      else:
          print(colored(f"SyntaxError on line {ln}: invalid operator(s)", "red"))
    except KeyError:
      print(colored(f"VarError on line {ln}: Undefined Variable was referenced", "red"))
# SimpleScript X shell
def SimpleScriptX(text, code, ln=0): 
    global DEFINING_FUNCTION
    global functionName
    global executing

    for i in text:
        try:
            getval(i)
        except: pass
    
    ln += 1
    # Turn variables into their values
    for i in text:
        if i[0] == "$":
            ia = i.replace(i[0], '')
            if ia in variables:
                i = variables[ia]
            else:
                pass

    if code == "end function":
        DEFINING_FUNCTION = False
    if DEFINING_FUNCTION and code != "end function":
        functions[functionName].append(code)
    elif code == "end function":
        pass
    elif len(text) == 0:
        pass
    # "var" command
    elif text[0] == "var":
        code = code.replace('\s',' ')
        splitter = code.find('=') + 1
      
        if text[2] == "=" and code.find('+')!=-1 or code.find('-')!=-1 or code.find('*')!=-1 or code.find('/')!=-1 or code.find('%')!=-1:
            variables[text[1]] = str(process_math(text[3:],code))
        elif text[2] == "=" and text[3] == "readFile":
            with open(text[4], 'r') as file:
                variables[text[1]] = str(file.read())
        elif text[2] == "=" and text[3] == "readFileLines":
            with open(text[4], 'r') as file:
                variables[text[1]] = str(file.read()).split('\n')
        elif text[2] == "=" and text[3] == "from" and text[5] == "get":
            try:
                if text[6][0] == "$": index = int(variables[text[6][1:]])
                else: index = int(text[6])
                variables[text[1]] = variables[text[4]][index]
            except ValueError:
                cprint(
                    f"IndexError at Line {ln}: List index does not exist: {index}",
                    'red')
        elif text[2] == "=":
            variables[text[1]] = getval(code.replace('\s',' ')[splitter:])
        elif text[1] == "list":
            if text[4] == "split" and text[6] == "by":
                if text[5][0] == "$":
                    variables[2] = variables[text[5]].split(text[7])
                else:
                    variables[2] = text[5].split(text[7])
            elif text[4][0] == "$" or text[-1][0] == "$":
                variables[text[2]] = process_math(text,code)
            else:
                value = code.replace(f"var list {text[2]} = ", "")
                variables[text[2]] = value.split(",")
        else:
            print(colored(f"SyntaxError on line {ln}", "red"))

    # prompt
    elif text[0] == "prompt":
        code = code.replace(f'prompt {text[1]} = ','')
        string = ""
        for i in code.split():
          string += getval(i) + ' '
        variables[text[1]] = input(string)

    # "print" command
    elif text[0] == "print":
        text.remove(text[0])
        string = ''
        for i in text:
            string += str(getval(i)) + ' '  # Add to string to be printed
        string = string.replace('\\n', '\n')
        string = string.replace('\\t', '\t')

        print(string)

    elif text[0] == "printx":
        color = getval(text[1])
        text.remove(text[0])
        text.remove(text[0])
        string = ''
        if text[0][0] == "$":  # If printing var
            string += str(variables[text[0].replace(
                "$", "")]) + " "  # Add to string to be printed
        else:
            for i in text:
                string += i + ' '  # Add to string to be printed
        string = string.replace('\\n', '\n')
        string = string.replace('\\t', '\t')

        print(colored(string, color))

    # "help" command
    elif text[0] == "help":
        cprint(
            "Here is a list of available commands:\n\n",
            sys_color,
            attrs=['bold'])
        string = ''
        for i in commands:  # Iterates through keys of Dict commands
            string += i + '        ' + commands[i] + '\n'
        cprint(string, sys_color, attrs=['bold'])

    # Math
    elif len(text) > 2 and text[1] in math:
        result = process_math(text,code)
        print(result)

    elif text[0][0] == '*':
        pass

    # exit
    elif text[0] == 'exit':
        executing = False
        #exec('exit()')
    # clear
    elif text[0] == "clear":
        print("\033[H\033[2J")

    # write
    elif text[0] == "write" and text[-2] == "to":
        string = str(getval(code.replace("write ", "").replace(" to ", "").replace(
            f"{text[-1]}", "")))
        with open(getval(text[-1]), 'a') as file:
            file.write(string)

    elif text[0] == "function":
        alist = []
        functionName = text[1]
        functions[functionName] = alist
        DEFINING_FUNCTION = True

    elif text[0] in functions:
        cs = functions[text[0]]
        for command in cs:
            SimpleScriptX(command.split(), command)

    elif text[0] == "exec" or text[0] == "execute":
        open_file(text[1])

    elif text[0] == "if":
        if text[2] == "==" or "=":
            if text[1][0] == '$':
                text[1] = text[1].replace(text[1][0], '')
                if text[1] in variables:
                    text[1] = variables[text[1]]
                else:
                    print(colored(f"Variable \"{text[1]}\" not found", "red"))
            if text[1] == text[3]:
                cs = functions[text[4]]
                for command in cs:
                    SimpleScriptX(command.split(), command)
            else:
                if text[5] == "else":
                    cs = functions[text[6]]
                    for command in cs:
                        SimpleScriptX(command.split(), command)

    elif text[0] == "loop":
        for i in range(int(getval(text[1]))):
            cs = functions[text[2]]
            for command in cs:
                SimpleScriptX(command.split(), command)

    elif text[0] == "shell":
        text.remove(text[0])
        string = ''
        for i in text:
            string += i + ' '
        os.system(string)
    
    # unknown command
    else:
        cprint("Unknown Command", 'red')
        # raise SyntaxError(f"Unknown Command: {text[0]}")


def open_file(filename):
    with open(filename, 'r') as file:
        data = file.readlines()  # Each line as element of list
        data = [x.strip() for x in data]  # Remove spaces and \n
        for i in data:
            SimpleScriptX(i.split(),
                          i)  # Split lines into parts and process them


open_file('test.simplescriptx')  # Runs SimpleScript X from file

while executing:  # Runs SimpleScript X in the shell
    if DEFINING_FUNCTION:
        code = input(colored("\t> ", "red"))
    else:
        code = input(colored("> ", "red"))
    try:
        SimpleScriptX(code.split(), code)
    except KeyError:
        cprint(f"VarError on Line {ln}: An undefined variable was used.",
               "red")
   # except Exception as e:
        #cprint(f"SyntaxError on line {ln}", "red")
        #cprint(f"Error on line {ln}: {e}","red")
