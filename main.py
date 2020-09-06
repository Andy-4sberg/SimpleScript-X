"""
Credits (repl.it):
@Andy_4sberg
@DavidShen2
"""
# Setup
import os, random,time,datetime
from termcolor import colored, cprint
print("\033[H\033[2J") # Clear Screen
shell,math,logic,sys_color,functionName,commands,executing,COMMENTING,variables,functions,version,DEFINING_FUNCTION,ln = "> ",["+","-","*","/","%"],["==",">=","<=",">","<","!=","!","="],"blue","",{"help": "Shows all available commands","print": "Prints text to the screen","printx": "prints colored text to the screen","var": "Creates a variable","var list": "Creates a list","*": "Creates a comment","prompt": "Asks for user input","exit": "Exits SimpleScript X","clear": "Clears the screen","write x to file": "Writes x to file"},True,False,{},{},["1.4.3", "beta"],False,0 # It's faster for python to read it like this.

result = " "
def getval(var):
    if var[0] == "$" and var[1:] in variables:
        try:return float(variables[var[1:]])
        except ValueError:return variables[var[1:]]
        except TypeError:return variables[var[1:]]
    else:
        try:return float(var)
        except ValueError:return var
        except TypeError:return var

def process_math(text, full):
      global code
      full = full.split(' = ', 1)[-1]
      if '+' in text:
        a = full.split(' + ', 1)[0]
        if ',' in a: a=a.split(',')
        a,b = getval(a),full.split(' + ', 1)[-1]
        if ',' in b: b=b.split(',')
        b = getval(b)
        return(a+b)

      elif '-' in text:
        a = full.split(' - ', 1)[0]
        if ',' in a: a=a.split(',')
        a,b = getval(a),full.split(' - ', 1)[-1]
        if ',' in b: b=b.split(',')
        b = getval(b)
        if isinstance(a,list) and isinstance(b,list):
          return(list(set(a) - set(b)))
        else:
          return(a-b)

      elif text[1] == '*':
        a,b = getval(text[0]),getval(text[2])
        return(a*b)
      elif text[1] == '/':
        a,b = getval(text[0]),getval(text[2])
        return(a/b)

      elif text[1] == '%':
        a,b = getval(text[0]),getval(text[2])
        return(a % b)
      else:
          print(colored(f"SyntaxError on line {ln}: invalid operator(s)", "red"))
def run_logic(a,operator,b):
  if operator in logic:
    a,b = getval(a),getval(b)
    if operator=="==": return bool(a==b)
    elif operator==">=": return bool(a>=b)
    elif operator=="<=": return bool(a<=b)
    elif operator==">": return bool(a>b)
    elif operator=="<": return bool(a<b)
    elif operator=="!=": return bool(a!=b)
    elif operator=="=": return bool(a==b)
    elif operator=="!": return bool(a!=b)
  else: cprint("Invalid Logic Operator","red")
# SimpleScript X shell
def SimpleScriptX(text, code):
    try:
        text_2 = text[0].lower()
        text[0] = text_2
    except IndexError:
        pass
    global ln,functionName,executing,COMMENTING,DEFINING_FUNCTION,result,compiled
    ln += 1

    if text==['']:pass
    elif len(text)==0:pass
    elif text[0]=="***" and not COMMENTING:COMMENTING=True
    elif text[0]=="***" and COMMENTING:COMMENTING=False
    elif COMMENTING:pass
    elif code=="end function":DEFINING_FUNCTION=False
    elif DEFINING_FUNCTION and code !="end function":functions[functionName].append(code)
    elif code=="end function":pass

    # "var" command
    elif text[0]=="var":
        code,splitter=code.replace('\s',' '),code.find('=')+2
        if text[1]=="random"and text[3]=="="and text[2]!="=":variables[text[2]]=random.randint(int(text[4]),int(text[5]))
        elif text[2] == "=" and text[3] == "getTime": variables[text[1]] = time.time()
        elif text[2] == "=" and text[3] == "getDateTime": variables[text[1]] = datetime.datetime.now()
        elif text[2] == "=" and any(i in text[3:] for i in math):variables[text[1]] = str(process_math(text[3:],code))
        elif text[2] == "=" and text[3] == "readFile":
            with open(text[4], 'r') as file:variables[text[1]] = str(file.read())
        elif text[2] == "=" and text[3] == "readFileLines":
            with open(text[4], 'r') as file:variables[text[1]] = str(file.read()).split('\n')
        elif text[2] == "=" and text[3] == "from" and text[5] == "get":
            try:variables[text[1]] = variables[text[4]][int(getval(text[6]))]
            except ValueError:cprint(f"IndexError at Line {ln}: List index does not exist: {int(getval(text[6]))}",'red')
        elif len(text)>4 and text[2] == "=" and text[4] == "getIndex":
            variables[text[1]] = variables[text[3]].index(getval(text[5]))
        elif text[2] == "=":variables[text[1]] = getval(code.replace('\s',' ')[splitter:])
        elif text[1] == "list":
            if text[4] == "split" and text[6] == "by":variables[2] = variables[text[5]].split(str(getval(text[7])))
            elif text[4][0] == "$" or text[-1][0] == "$":variables[text[2]] = process_math(text,code)
            else:
                value = code.replace(f"var list {text[2]} = ", "")
                value = value.split(",")
                variables[text[2]] = [getval(x) for x in value]
        else:print(colored(f"SyntaxError on line {ln}", "red"))

    # prompt
    elif text[0] == "prompt":
        code,string = code.replace(f'prompt {text[1]} = ',''),""
        for i in code.split():string += getval(i) + ' '
        variables[text[1]] = input(string)

    # "print" command
    elif text[0] == "print":
        text.remove(text[0])
        string = ''
        for i in text: string += str(getval(i)) + ' '  # Add to string to be printed

        string = string.replace('\\n', '\n')
        string = string.replace('\\t', '\t')        
        print(string)

    elif text[0] == "printx":
        color,string = getval(text[1]),''
        text.remove(text[1])
        text.remove(text[0])
        for i in text:string += str(getval(i)) + ' '  # Add to string to be printed
        string = string.replace('\\n', '\n')
        string = string.replace('\\t', '\t')
        cprint(string,color)

    # "help" command
    elif code.strip() == "help":
        cprint("Here is a list of some available commands:\n\n",sys_color,attrs=['bold'])
        string = ''
        for i in commands:
            string += i.ljust(20, ' ') + commands[i] + '\n'
            if len(i) == 20:pass
            else: i += ' '
        cprint(string, sys_color, attrs=['bold'])

    # Math
    elif len(text) > 2 and text[1] in math:
        result = process_math(text,code)
        print(result)

    elif text[0][0] == '*':pass
    # exit
    elif text[0] == 'exit':executing = False
    # clear
    elif text[0] == "clear":print("\033[H\033[2J")

    # write
    elif text[0] == "write" and text[-2] == "to":
        string = str(getval(code.replace("write ", "").replace(" to ", "").replace(f"{text[-1]}", "")))
        with open(getval(text[-1]), 'a') as file:file.write(string)

    elif text[0] == "function":
        alist,functionName,DEFINING_FUNCTION = [],text[1],True
        functions[functionName] = alist

    elif text[0] in functions:
        cs = functions[text[0]]
        for command in cs:SimpleScriptX(command.split(), command)


    elif text[0] == "exec" or text[0] == "execute":
        run_file(text[1])


    elif text[0] in variables and text[1]=="set" and text[3]=="as":
        variables[text[0]][int(text[2])] = getval(text[4])
    elif text[0] == "if":
      text.pop(0)
      tf,cmds = run_logic(text[0],text[1],text[2]),code.replace(f'if {text[0]} {text[1]} {text[2]} ','')
      if tf:
        cmds,cmds2 = cmds.split(';;;'),[]
        for x in cmds:
          if 'else' in x:break
          else: cmds2.append(x)
        for cmd in cmds2: result = SimpleScriptX(cmd.split(),cmd)
      else:
        try:
            cmds2 = cmds.split('else')[1].split(';;;')
            for cmd in cmds2: result = SimpleScriptX(cmd.split(),cmds.split('else')[1].split(';;;'))
        except:
            pass
      return result

    elif text[0] == "license":
        license,string = open("LICENSE","r").readlines(),''
        for i in license:
            string += i+'\n'
        print(string)

    elif text[0] == "loop":
        if len(text)>1 and (getval(text[1]) == "FOREVER" or text[0]=="break"): 
          cmds = code.replace(f"loop FOREVER ","").split(';;;')
          while 1:
            for command in cmds:
                if result == "break":command="break"
                if command == "break": break
                result = SimpleScriptX(command.split(), command)
                
            if command == "break": break
          result = " "
        else:
          cmds = code.replace(f"loop {text[1]} ","").split(';;;')

          for i in range(int(getval(text[1]))):
            for command in cmds:
                if result == "break":command="break"
                if command == "break":break
                result = SimpleScriptX(command.split(), command)
                
            if command == "break":break
          result = " "
    elif text[0] == "break":
        return ("break")
    elif text[0] == "wait": time.sleep(getval(text[1]))
    elif text[0] == "shell":
        code = code.replace(text[0],"")
        os.system(code)

    elif text[0] == "remove":
        variables.pop(text[1])
    
    elif text[0] == "repl.it":print(colored(f"SyntaxError on line {ln}: repl.it is a website, not a command.",'yellow'))

    elif text[0] == "length":
        if text[2] == "=":variables[text[1]] = len(getval(text[3]))

    # unknown command
    else:cprint(f"\nSyntaxError on Line {ln}: Unknown Command in: \"{code}\" ","red")

def run_file(filename):
  try:
    with open(filename, 'r') as file:
        data = file.readlines()  # Each line as element of list
        data = [x.strip() for x in data]  # Remove spaces and \n
        for i in data:
            SimpleScriptX(i.split(),i)  # Split lines into parts and process them
  except KeyError:cprint(f"VarError on Line {ln}: An undefined variable was used.","red")
  except KeyboardInterrupt:cprint(f"KeyboardInterrupt","red")
  except FileNotFoundError:cprint(f"File{filename} does not found.",'red')
  except:cprint(f"SyntaxError on line {ln}","red")#cprint(f"Error on line {ln}: {e}","red")

run_file('start.simplescriptx')  # Runs SimpleScript X from file
if __name__ == '__main__':
    cprint(f"SimpleScript X v{version[0]} ({version[1]})\n\nType \"help\" for a list of commands\n\n",sys_color,attrs=['bold'])  # Displays version on startup
    while executing:  # Runs SimpleScript X in the shell
        try:
            if DEFINING_FUNCTION:code = input(colored("\t> ", "red"))
            else:code = input(colored("> ", "red"))
            if code == '': pass
            elif code.strip() == '': pass
            else:
                try:SimpleScriptX(code.split(), code)
                except KeyError:print(colored(f"VarError on Line {ln}: An undefined variable/function was used.","red"))
                except:print(colored(f"SyntaxError on line {ln}", "red"))
        except KeyboardInterrupt:
            print(colored(f"\nKeyboardInterrupt","red"))
            executing = False
else:pass