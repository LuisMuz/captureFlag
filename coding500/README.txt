Hello adventurer!

Here's a secret code that you have to parse.
If you are able to translate and execute it... Maybe you can find a useful key to get a lot of points.

For each level you can find a source file with a program wrote in a strange language that you have to execute, and an example file.
Following the comments in the example file will help you to understand the underlying grammar of the language and translate correctly.

Comments begin with '//'. After the two slashes, everything following in-line must not be considered or executed

You will have to handle two TYPEs of objects:
- INTEGERS, both POSITIVE and NEGATIVE (N.B.: there could be very loooong numbers, watch out);
- STRINGS, composed only by LOWER CASE characters, '.' and '_'.

VARIABLES could store INTEGER or STRING values, and their names are composed by at least a lower case character followed by an arbitrary number of lower case characters and digits.

There could be two types of INSTRUCTION in this language:
- PRINT: this instruction prints on console the value of one object passed
- ASSIGNMENT: this type of instructions represent in a common language the pattern <variable> = EXPR

EXPR could contain some OPERATIONS on objects of type integers, strings or variables.
OPERATIONS are ADD, SUB, MUL and DIV. Not all operations are appropriate to all object types.
Note: Of course, operations are only allowed on objects of the same type (for example, it's not allow to have number+string).

Here's another little suggestion: UPPER CASE characters in the grammars mean something important every time, differently from space that most of the time means nothing.

Good luck!


---
IMPORTANT! - Some tools for opening encrypted zip files show some issues in decrypting the zip containing the flag. Please don't trust the windows explorer unzip tool on Windows machine or unzip also in Unix machine. Use instead other tools such as for example 7zip.