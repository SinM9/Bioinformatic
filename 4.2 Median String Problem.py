
'''
CODE CHALLENGE: Implement MedianString.
     Input: An integer k, followed by a collection of strings Dna.
     Output: A k-mer Pattern that minimizes d(Pattern, Dna) among all k-mers Pattern. (If there are
     multiple such strings Pattern, then you may return any one.)
Sample Input:

5
GAAACTACGCACGTAGTGTTTTGCTACGGTTCTCA
TATATCCACATGACCTCGACAACGCACGGTCGAAT
TAGCGGGACAATCAGGTCTGAGTCGACTGTTGTGC
TCCTGCCGGTTGCTAACTGTAGACGTTTACCCCTT
TCCCTCCCTAACTCTAGGCTACTGTCGTCCGCAGT
AGGCAGAAAGACAACGGTAGTAATCTAGAGACCGT
CGCTCCACGCAGCTCATAGAACCGTGTTGTTCAAC
ACTGTCTCCCGGAAACCATAAACTACTTGGTTTGT
GGTTTTCTTGACTGTAATTACAATCCAGGAGACCA
ATGTCGCTCTACAGTGAACACGTAACTGTCTTCGG
Sample Output:

ACTGT
'''

def ATGC_Combinations(k):
    bases = ['A', 'C', 'G', 'T']
    array = ['A', 'C', 'G', 'T']
    for n in range(k - 1):
        array1 = []
        for i in array:
            for j in bases:
                array1.append(i + j)
        array = array1
    return array   

def Hamming_Distance(p, q):
    distance = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            distance += 1 
    return distance

def Min_Hamming_Distance(s1, s2):
	distance = len(s1)
	for i in range(len(s2) - len(s1) + 1):
		tmp = 0
		for j in range(len(s1)):
			if s1[j] != s2[i:i+len(s1)][j]:
				tmp += 1
		if  distance > tmp:
			distance = tmp
	return distance

def FindMedianString(DNA, k):
    res=[]
    p = ATGC_Combinations(k)
    distance = {}
    min_s = len(DNA) * len(p)
    for i in p:
        count = 0
        for j in range(len(DNA)):
            count += Min_Hamming_Distance(i, DNA[j])
        distance[i] = count
        if min_s > count :
            min_s = count
    for i in distance.keys():
        if (distance[i] == min_s):
            res.append(i)
    return res
#################################################################################
k= int(input())
DNA = []
i=0
while True:
    try:
        DNA.append(str(input())) 
    except EOFError:
        break
    
#print(DNA)
res=[]
res=FindMedianString(DNA, k)
#for i in range(len(res)):
   # res1=str(res[i])
    #print(str(res1))
res1=str(res[0])    
print(str(res1))
