Changes Log: A document documenting the changes made to SimpleScript X.

**************************************

8/13/20:
---
Fixed scope issue with compile and ln
Fixed print $Variable
Fixed help command
Fixed running scripts from a file
Converted "print" to "cprint" from termcolor package
Cosmetic updates
--- Changes Made by DavidShen2

**************************************

8/14/20:
---
Fixed error message when typed blank line
Added simple math operations
Added comments
Added user input (prompt)
##### --- Changes Made by Andy_4sberg
---
Fixed assignment issue with two variables
Added math operations for variables
--- Changes Made by DavidShen2

**************************************

8/15/20:
---
Fixed clear command
Fixed exit command
Added ability to do things like: var test = 8 + 3 and var test 2 = $test + 9
Fixed blank line issue
Revised user input
Added list
Added add ___ to LIST ability to list
Added remove ___ from LIST ability to list
--- Changes Made by DavidShen2

**************************************

8/16/20:
---
Added '\n' and '\t' tags tp 'print' command
Changed comments (no space required)
Added "printx" command
--- Changes Made by Andy_4sberg

---
Tried to fix lists. (Huge issues, some progress)
--- Changes Made by DavidShen2

**************************************

8/17/20
---
Lists now work
process_math() has been moved to math_processer.py
Added functions
Worked on Documentation
--- Changes Made by DavidShen2

---
Started "if" command (can't use vars yet)
Fixed a bug
--- Changes Made by Andy_4sberg

**************************************

8/18/20 - * * * V1 RELEASED * * *
---
Added string splitting
Added readFileLines (returns list)
Documentation
Code and Error Cleanup
--- Changes Made by DavidShen2

**************************************

8/19/20: Improvements

**************************************

8/20/20:
---
Forever Loops
Break Statement in Loops
C version
--- Changes Made by DavidShen2

**************************************

8/21/20:
---
Added random
Made program faster and more efficient
Fixed bugs
Fixed typo in help (removed "print $")
Commands no longer have to be lowercase
##### --- Changes Made by Andy_4sberg
---
Fixed bugs
Improvements to if else
Added Multi-line comments
##### --- Changes Made by DavidShen2

**************************************

8/22/20:
---
Improvements to Loops
Helped fix "help" command
##### --- Changes made by DavidShen2
---
Helped fix "help" command
Fixed bug
--- Changes made by Andy_4sberg

**************************************

8/23/20:
---
Added getTime 
Added getDateTime
Added wait ___
--- Changes made by DavidShen2

8/31/20:
---
FIXES, FIXES, FIXES, FIXES, FIXES, FIXES, FIXES, FIXES, FIXES, FIXES, FIXES, FIXES, FIXES, FIXES, FIXES, FIXES, FIXES, FIXES, FIXES, FIXES, FIXES, FIXES, FIXES, FIXES, FIXES, FIXES, FIXES, FIXES, FIXES, FIXES, FIXES, FIXES, FIXES, FIXES, FIXES, FIXES, FIXES, FIXES, FIXES, FIXES, FIXES, FIXES

My head has imploded now.

Added remove 
--- Changes made by DavidShen2

**************************************

9/3/20:
---
Fixes
Added new features I'm to lazy to mention
--- Changes made by Andy_4sberg

10/14/20:
---
Changed "printx" command
###### Syntax: printx {COLOR}TEXT{ANOTHER COLOR}
###### Color applies to everything on that line (unless changed by another color)
Added "promptx" command (colored user input)
###### Syntax: promptx NAME = {COLOR}TEXT{COLOR}
###### Color applies to everything on that line (unless changed by another color)
Added "color" function
###### Syntax: color(string)
###### turns {COLOR} into color
--- Changes made by Andy_4sberg