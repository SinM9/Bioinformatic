
'''
CODE CHALLENGE: Cyclopeptide Scoring Problem.
Cyclopeptide Scoring Problem: Compute the score of a cyclic peptide against a spectrum.
     Input: An amino acid string Peptide and a collection of integers Spectrum.
     Output: The score of Peptide against Spectrum, Score(Peptide, Spectrum).
Sample Input:

NQEL
0 99 113 114 128 227 257 299 355 356 370 371 484
Sample Output:

11
'''
S=str(input())
Spectrum = list(map(int, input().split()))
M=[57,71,87,97,99,101,103,113,113,114,115,128,128,129,131,137,147,156,163,186]
MASS={'G':57,'A':71,'S':87,'P':97,'V':99,'T':101,'C':103,'I':113,'L':113,'N':114,'D':115,'K':128,'Q':128,'E':129,'M':131,'H':137,'F':147,'R':156,'Y':163,'W':186}

SUBP=[]
s=S+S
for k in range(1, len(S)):
	for j in range(0,len(S)):
		subpep = s[j:j+k]
		SUBP.append(subpep)
SUBP.append(S)

sum=0
SUM=[]
SUM.append(0)
for i in range(0, len(SUBP)):
    st=list(SUBP[i])
    for j in range(0, len(st)):
        sum=sum+MASS[st[j]]
    SUM.append(sum)
    sum=0
SUM.sort()    
#for i in range (len(SUM)):
    #print(SUM[i])

'''
c=0
for i in range(len(Spectrum)):
    if Spectrum[i] in SUM:
       c+=1
       if Spectrum.count(i)==SUM.count(i)==2:
            c+=Spectrum.count(i)
print(c)
'''
score = 0
for item in SUM:
    if item in Spectrum:
        score += 1
        Spectrum.remove(item)
print (score)
