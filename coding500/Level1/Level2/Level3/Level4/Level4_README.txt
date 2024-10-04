//This is the last level, where you'll meet the last kind of instruction: the LOOP one
//As for BOH, LOOP statements will always be on separated lines from different operations too.
//And at this time you should correctly imagine that there could be a BOH inside a LOOP, but also a LOOP inside a BOH and a LOOP inside a LOOP...  
//
//Everything you need to know it's already in your mind: good luck!

//BEGIN EXAMPLE1
N1s1Vir= 
POOL VirP  VirN1s0ADDVir=  | VirN1a4m2s5TL LOOP 
//END EXAMPLE1: Prints numbers from 1 to 5

//BEGIN EXAMPLE2:
N1s1Vvrarrr1r=
POOL Vvrarrr1rN1s0ADDVvrarrr1r=  Vvrarrr2rP  Vvrarrr1rN0a1m2a1ADDVvrarrr2r=  | Vvrarrr1rN1a0m2a3TL LOOP
//END EXAMPLE2: Prints numbers from 3 to 7 

//BEGIN EXAMPLE3:
N1s1Vir= N1s1Vtrorprrrirnrtr=
POOL VirN1s0ADDVir=  HOB VirP  | VtrorprrrirnrtrN1s0QE BOH  | VirN0a1m2a3TL LOOP
//END EXAMPLE3: it doesn't print anything

//BEGIN EXAMPLE4:
N1s1Vir= N1s0Vsrerprarrrartrer= B.bVsrerprarrrartrorrr=
POOL VirN1s0ADDVir=  HOB VsrerprarrrartrorrrP  | VsrerprarrrartrerN1s0QE AND VirN2m2EN BOH  VirP  | VirN0a4m2s3TL LOOP
//END EXAMPLE4: prints "0.1.2.3.4"

//BEGIN EXAMPLE5:
N2Vjr= N1s0Vir=
POOL N2Vjr=  VirN1s0ADDVir=  B.b.b.bP  POOL VjrN1s0ADDVjr=  VmrurlrP  B.bP  VirVjrMULVmrurlr=  | VjrN1a1m2a1EL LOOP  VirP  | VirN2m2EL LOOP
//END EXAMPLE5: Prints "1.2.3.4.5...2.4.6.8.10...3.6.9.12.15...4.8.12.16.20..."

//BEGIN EXAMPLE6:
N1s1Vprrrirnrtrmrurlrtrirprlrirerrrsr= N2Vjr= N1s0Vir=
POOL N2Vjr=  VirN1s0ADDVir=  B.b.b.bP  HOB POOL VjrN1s0ADDVjr=  VmrurlrP  B.bP  VirVjrMULVmrurlr=  | VjrN1a0m2a3EL LOOP  | VprrrirnrtrmrurlrtrirprlrirerrrsrN1s0QE BOH  VirP  | VirN1a2m2s1TL LOOP
//END EXAMPLE6: Prints "1...2...3...4..."
