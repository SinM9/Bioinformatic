
'''
CODE CHALLENGE: Implement GreedyMotifSearch.
    Input: Integers k and t, followed by a collection of strings Dna.
    Output: A collection of strings BestMotifs resulting from applying GreedyMotifSearch(Dna,k,t).
    If at any step you find more than one Profile-most probable k-mer in a given string, use the
    one occurring first.
Debug Datasets

Sample Input:

5 5
TCCCTCCATGTGTAAAGTCCGCCTCTACTTCGAGT
GGTAGTACCCCTCTAGAATTATTATCCTTAGGTCA
CACGTCGAGGACCGCCGCCGCCATCACAAGCTTTA
GCAATGATCCCCGTTTACATCAATAGAGGGGGGAA
GACGACCCTAGCTTCTTCTTGAGTTTGTGAAGCGG
Sample Output:

CCCTC
CCCTC
CACGT
CCCGT
GACGA
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

def MostProbKmer(DNA, k, Matr):
    seq = {}
    for i in range(len(DNA) - k + 1):
        seq[DNA[i:i + k]] = ProbKmer(DNA[i:i + k], Matr)
    for i in seq.keys():
        if seq[i] == max(seq.values()):
            return i
            
def Profile(M):
    k = len(M[0])
    Prof=[[0] * k for i in range(4)]
    for st in M:
        for i in range(len(st)):
            if st[i] == "A":
                Prof[0][i] += (1/len(M))
            if st[i] == "C":
                Prof[1][i] += (1/len(M))
            if st[i] == "G":
                Prof[2][i] += (1/len(M))
            if st[i] == "T":
                Prof[3][i] += (1/len(M))           
    return Prof          
            
            
def GreedyMotifSearch(DNA, k, t):
    res = []
    for st in DNA:
        res.append(st[0:k])
    for i in range(len(DNA[0])-k+1):
        M = []
        M.append(DNA[0][i:i+k])
        for j in range(1,t):
            M.append(MostProbKmer(DNA[j], k, Profile(M)))
        if Score(res) > Score(M):
            res = M
    #print(res)
    return res


def Score(motifs):
    res=0
    st = ""
    profile = Profile(motifs)
    for i in range(len(profile[0])):
        max_p = 0
        sym = 0
        for sym in range(4):
            if profile[sym][i] > max_p:
                s = sym
                max_p = profile[sym][i]
        if s == 0:
            st+="A"
        if s == 1:
            st+= "C"
        if s == 2:
            st+= "G"
        if s == 3:
            st+= "T"      
    for string in motifs:
        for i in range(len(string)):
            if st[i] != string[i]:
                res += 1
    return res
######################################################
k, t = map(int, input().split())
DNA = []
for i in range(t):
    DNA.append(str(input())) 
res=GreedyMotifSearch(DNA, k ,t)
for i in res:
	print(i)