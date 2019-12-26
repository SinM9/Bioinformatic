
'''
Profile-most Probable k-mer Problem: Find a Profile-most probable k-mer in a string.
     Input: A string Text, an integer k, and a 4 × k matrix Profile.
     Output: A Profile-most probable k-mer in Text.

CODE CHALLENGE: Solve the Profile-most Probable k-mer Problem.

Debug Datasets

Sample Input:

CCCCTATAGTTCTTGGTGCAGCGTGCACCCTCGTCTGGTTCGGATACGGGCCTGCCAGGA
5
0.583 0.25 0.417 0.25 0.167
0.083 0.25 0.417 0.333 0.25
0 0.25 0.167 0 0.333
0.333 0.25 0 0.417 0.25
Sample Output:

ATACG
'''

def ProbKmer(s, matr):
	P = 1
	for i in range(len(s)):
		if s[i] == 'A':
			P = P * matr[0][i]
		if s[i] == 'C':
			P = P * matr[1][i]
		if s[i] == 'G':
			P = P * matr[2][i]
		if s[i] == 'T':
			P = P * matr[3][i]
	return P
######################################################
DNA=str(input())
k= int(input())
#Matr=[[]]
Matr=[[0] * k for i in range(4)]
tmp=[]
for i in range (4):
    tmp=list(map(float, input().split()))
    for j in range(k):
        Matr[i][j]=tmp[j]
#print (Matr)
seq = {}
for i in range(len(DNA) - k + 1):
    seq[DNA[i:i + k]] = ProbKmer(DNA[i:i + k], Matr)
for i in seq.keys():
    if seq[i] == max(seq.values()):
        print(i)