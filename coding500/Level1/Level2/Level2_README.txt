//Welcome to the second level
//Time to add a new instruction: the 'BOH' statement
//A 'BOH' statement is composed by a COND and a list of INSTRUCTIONS.
//inside the BOH there could be an alternative, called OH, which have also its COND and instructions' list.
//Only one of them will be executed, but remember that the OH is not always present.
//
//RULES1: entire BOH statements lies always on a single line
//RULES2: CONDs are evaluated from LEFT TO RIGHT
//RULES3: each COND is always binary, and there are new operations for them (es. QE, EL, ...)
//
//BOH statements will always be on separated lines from different operations.

//BEGIN EXAMPLE1
N2m4m3Vvrarrr2r= N2a4m3d2s1m5a2Vvrarrr1r=
var2 = 24, var1 = 42
HOB HO Vvrarrr2rP | N1s1N1s1QE OH Vvrarrr1rP | Vvrarrr1rN50a2s10QE BOH
HO 0_0QE 42_42QE => print 42 
//END EXAMPLE1: Prints 42

//BEGIN EXAMPLE2
N2m4m3d2Vvrarrr2r= N2a4m3d2s1m5a2Vvrarrr1r=
var2 = 12, var1 = 42
HOB HO Vvrarrr2rP | N1s1N1s1QE OH Vvrarrr1rP | Vvrarrr1rN50a2s10EL BOH
HO 0_0QE 42_42EL => do 2
//END EXAMPLE2: Prints 42

//BEGIN EXAMPLE3
N2m4m3d2Vvrarrr2r= N2a4m3d2s1m5a2Vvrarrr1r=
var2 = 12, var1 = 42
HOB HO Vvrarrr2rP | N1s1N1s1QE OH Vvrarrr1rP | Vvrarrr1rN50a2s10TL BOH
0_0QE 42_42TL => do 1
//END EXAMPLE3: Prints 12

//BEGIN EXAMPLE4
N2m4m3d2Vvrarrr2r= N2a4m3d2s1m5a2Vvrarrr1r=
var2 = 12, var1 = 42
HOB HO Vvrarrr2rP | N1s1N1s1QE OH Vvrarrr1rP | Vvrarrr1rN50a2s10TG BOH
0_0QE 42_42TG => do 1
//END EXAMPLE4: Prints 12
3r

//BEGIN EXAMPLE5
N2m4m3d2Vvrarrr2r= N2a4m3d2s1m5a2Vvrarrr1r=
var2 = 12, var1 = 42
HOB HO Vvrarrr2rP | N1s1N1s1QE OH Vvrarrr1rP | Vvrarrr1rN50a2s10EG BOH
0_0QE 42_42EG => do 2
//END EXAMPLE5: Prints 42

//BEGIN EXAMPLE6
N2m4m3d2Vvrarrr2r= N2a4m3d2s1m5a2Vvrarrr1r=
var2 = 12, var1 = 42
HOB HO Vvrarrr2rP | N1s1N1s1QE OH Vvrarrr1rP | Vvrarrr1rN1s1EN OR Vvrarrr1rN50a2s10TG BOH
0_0QE (42_0EN or 42_42TG) => do 2
//END EXAMPLE6: Prints 42

//BEGIN EXAMPLE7
N2m4m3d2Vvrarrr2r= N2a4m3d2s1m5a2Vvrarrr1r=
HOB HO Vvrarrr2rP | N1s1N1s1QE OH Vvrarrr1rP | Vvrarrr1rN1s1EN AND Vvrarrr1rN50a2s10TG BOH
//END EXAMPLE7: Prints 12

//BEGIN EXAMPLE8
N3m3Vvrarrr6r= N3m17Vvrarrr5r= N2m43Vvrarrr4r= 
var6 = 9, var5 = 51, var4 = 86
HOB HO Vvrarrr5rN1s0ADDVvrarrr6r=  | Vvrarrr6rVvrarrr6rQE OH Vvrarrr3rN0a0m2a3ADDVvrarrr6r=  | Vvrarrr5rVvrarrr4rQE BOH 
9_9QE 51_86QE => do 1
Vvrarrr6rP
//END EXAMPLE8: Prints 52 

//BEGIN EXAMPLE9
BhbsbiblbgbnbebVvrarrr3r= BoblblbebhbVvrarrr2r= BobabibcbVvrarrr1r=
var3 = english, var2 = hello, var1 = ciao
HOB HO Vvrarrr1rP  Vvrarrr1rBobdbnbobmbADDVvrarrr1r=  | Vvrarrr3rBnbabiblbabtbibQE OH Vvrarrr2rP  Vvrarrr2rBdblbrbobwbADDVvrarrr2r=  | Vvrarrr3rBhbsbiblbgbnbebQE BOH
english_italianQE english_englishQE => do 2
//END EXAMPLE9: Prints "helloworld" 

//BEGIN EXAMPLE10
N1s0Vfrlrargr=
flag = 1
HOB BhbobsbtbibtbubobhbtbibwbhbobbbebnboblbabrbobobpbabP  | VfrlrargrN1s0EN BOH 
1_1EN => nothing
//END EXAMPLE10: it doesn't print anything...

//BEGIN EXAMPLE11
N1a2m3Vfrlrargr= 
flag = 9
HOB BhbobsbtbibtbubobhbtbibwbhbobbbebnboblbabrbobobpbabP  | VfrlrargrN1s0EN BOH
9_1EN => true
//END EXAMPLE11: Prints "apooralonebohwithoutitsoh"

EN >
EG >=
EL <=
QE ==
TG !=
TL <
0_0QE 42_42QE => do 2
0_0QE 42_42EL => do 2
0_0QE 42_42TL => do 1
0_0QE 42_42TG => do 1
0_0QE 42_42EG => do 2
0_0QE (42_0EN or 42_42TG) => do 2
0_0QE (42_0EN and 42_42TG) => do 1
9_9QE 51_86QE => do 1
english_italianQE english_englishQE => do 2
1_1EN => false
9_1EN => true
42_42TG => false