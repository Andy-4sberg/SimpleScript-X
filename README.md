# Welcome to SimpleScript X!
#### SimpleScript X is a simple programming language built with Python that demonstrates to power of simplicity! 
![](https://repl.it/@SimpleScriptX/SimpleScript-X#Logo.png)
##### Variables:
Variables are denoted with "var" before variable name and defined by whatever comes after the equal sign.

    var VARIABLENAME = VALUE

To reference the value of a variable, place a "$" before the variable name:

    $VARIABLENAME
Variables can be defined by other variables:

    var variable1 = $variable2
Lists are variables that store multiple values. They are defined as follows:

    var list LISTNAME = ELEMENT1,ELEMENT2,ELEMENT3   *LISTNAME contains 3 elements.
To change a list, do as follows:

    var list list1 = $list1 + STUFF_TO_APPEND
    var list list1 = $list1 - STUFF_TO_REMOVE
You can append any variable to a list.
###### Remember the "list" keyword after "var"!
###### Important! All variables are global!     

##### Comments:
Comments are denoted by * before the comment.

    * This is a comment, it's just used as a note for developers
##### Print Statement:
Format: print followed by text or $variable


    var text = Hello World!    *Stores Hello World! to variable called text.
    print Hello World!    *Prints Hello World!
    print $text    *Prints value of text which is Hello World!

###### Important! Use spacing strictly as shown! Not doing so will cause errors or cause code to run incorrectly!

##### User Input:
User input is denoted by "prompt"

    prompt variable = text_to_display    *Input is stored to variable
##### Functions:
Functions are defined in the following multi-line format:

    function FUNCTION_NAME
    COMMAND_TO_EXECUTE1
    COMMAND_TO_EXECUTE2
    COMMAND_TO_EXECUTE3
    end function
Functions are called by their FUNCTION_NAME.

    FUNCTION_NAME    *This executes the function FUNCTION_NAME.
Example:

    function test
    print This is from function test!
    print This is again from test!
    end function  

    test    * Runs test
###### Tip: Function parameters can be passed by defining variables right before running the function since all variables are global.
##### If-else:
If-else commands require the use of functions. For example:

    function x 
    print test
    end function

    function y 
    print test2
    end function

    var variable = 8

    if variable == 8 x else y    * Outputs test

##### Loop
Loops are indicated by the keyword "loop". Loops also require functions the same way if-else statements require them. The syntax is as follows:

    loop NUMBER_OF_TIMES FUNCTION_NAME

Example:

    function X
    print test
    end function

    loop 10 X   * executes X 10 times

##### Math
The commands for math are the same as in nearly any other programming language.

    x + y     *Add
    x - y     *Subtract
    x * y     *Mulliply
    x / y     *Divide
    x % y     *Modulus

    var variable = 5 * 4
    var variable2 = $variable + 8    *variable2 is now 28

###### Important! Spacing, as always, is key!

##### File Handling
SimpleScript X can edit and read files.

    write CONTENT to FILE_NAME     *Writes CONTENT to FILE_NAME
    var stuff = readFile FILE_NAME    *Reads everything from FILE_NAME and stores that to the variable stuff
    var stuff2 = readFileLines FILE_NAME      *Reads everything from FILE_NAME and stores that to the variable stuff in the form of a list.

##### Shell commands
SimpleScript X supports system commands. 
Syntax:

    shell COMMAND
##### Other commands

    exit        *Exits SimpleScript X
    clear       *Clears console
    printx color_of_text text_to_display_in_color       *Prints text_to_display_in_color in color color_of_text
    exec FILE_NAME     *Runs SimpleScript X file
    help        *Outputs help menu