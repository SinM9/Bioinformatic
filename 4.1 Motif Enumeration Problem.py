
'''
CODE CHALLENGE: Implement MotifEnumeration.
     Input: Integers k and d, followed by a collection of strings Dna.
     Output: All (k, d)-motifs in Dna.

Sample Input:

4 1
CACTGATCGACTTATC
CTCCGACTTACCCCAC
GTCTATCCCTGATGGC
CAGGGTTGTCTTGTCT
Sample Output:

CAGA CCTT CTCT CTTA CTTG CTTT GACT GATT GCCT GGCT GTCT TATC TCTG TCTT TGAC TTAT TTTC
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

def Window(s, k):
    for i in range(1 + len(s) - k):
        yield s[i:i+k]

def in_window(combo, string, k, d):
    return any(Hamming_Distance(combo, pat) <= d for pat in Window(string, k))

def motif_enumeration(DNA, k, d):
    pattern = set()
    for combo in ATGC_Combinations(k):
        if all(in_window(combo, string, k, d) for string in DNA):
            pattern.add(combo)
    pt = list(pattern)
    return pt
###############################################################################
k, d = map(int, input().split(" "))

s1 = input()
s2 = input()
s3 = input()
s4 = input()

DNA =list()
DNA.append(s1)
DNA.append(s2)
DNA.append(s3)
DNA.append(s4)

res = motif_enumeration(DNA, k, d)
res.sort()
for i in range (len(res)):
    res1=str(res[i])
    print(res1)  