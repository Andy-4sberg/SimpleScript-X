# Welcome to SimpleScript X!
#### SimpleScript X is a simple programming language built with Python that demonstrates to power of simplicity! 
![](https://simplesite-x.simplescriptx.repl.co/logo.png)
##### Variables:
Variables are denoted with "var" before variable name and defined by whatever comes after the equal sign.

    var VARIABLENAME = VALUE

To reference the value of a variable, place a "$" before the variable name:

    $VARIABLENAME
Variables can be defined by other variables:

    var variable1 = $variable2
You can remove a variable as follows:

    remove VARIABLE_TO_REMOVE
Lists are variables that store multiple values. They are defined as follows:

    var list LISTNAME = ELEMENT1,ELEMENT2,ELEMENT3   *LISTNAME contains 3 elements.
To change a list, do as follows:

    var list list1 = $list1 + STUFF_TO_APPEND
    var list list1 = $list1 - STUFF_TO_REMOVE
You can append any variable to a list.
###### Remember the "list" keyword after "var"!
###### Important! All variables are global!     
###### Note: SimpleScript X keywords are NOT case-sensitive. Variables and functions are.
##### More on lists:
Individual elements can be changed by referencing the index. Syntax:

    LISTNAME set INDEX as NEW_ELEMENT
Strings can be split into a list with the following syntax:

    var list LISTNAME = split STRING by DIVIDER
You can obtain the index of an element in a list:

    var INDEX = LISTNAME getIndex ELEMENT
You can reference the element at an index:

    var ELEMENT = LISTNAME get INDEX

##### Comments:
Comments are denoted by * before the comment.

    * This is a comment, it's just used as a note for developers

Multi-line comments are marked by *** before and after the comment.

    ***
    Comments go 
    here....
    ***
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
If-else commands are followed by commands seperated by three semicolons. The logic operator must be "==",">=","<=",">","<","!=","!" or "=". "!" is equal to "!=" and "=" is equal to "==". For example:

    if 8 ! 7 print test;;;print test2 else print not working    * Outputs test test2

##### Loop
Loops are indicated by the keyword "loop". Commands to be looped must be seperated by three semicolons: ";;;" The syntax is as follows:

    loop NUMBER_OF_TIMES COMMAND1;;;COMMAND2;;;COMMAND3

Example:

    loop x print Hello!;;;print Hello Again
Use the break statement to break out of loops:

    loop 10 print test;;;break *Prints 'test'
##### Math
The commands for math are the same as in nearly any other programming language.

    x + y     *Add
    x - y     *Subtract
    x * y     *Mulliply
    x / y     *Divide
    x % y     *Modulus

    var variable = 5 * 4
    var variable2 = $variable + 8    *variable2 is now 28

You can use the math commands to concatenate strings and lists, remove elements from lists, and remove parts from strings.
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

##### Random
SimpleScript X now supports random variables, signaled by the "random" keyword. Syntax:

    var random variable = UPPER LOWER  *variable is random number between UPPER and LOWER
##### Time and Date
To get the current date:

    var DATE = getDateTime
To get the current time in a non-human friendly format:

    var TIME = getTime 
To make the program wait a few seconds:

    wait SECONDS_TO_WAIT
##### Other commands

    exit        *Exits SimpleScript X
    clear       *Clears console
    printx color_of_text text_to_display_in_color       *Prints text_to_display_in_color in color color_of_text
    exec FILE_NAME     *Runs SimpleScript X file
    help        *Outputs help menu
###### Tip: You can import another simplescriptx file's functions with exec FILE_NAME !