
'''
We say that a DNA string Pattern encodes an amino acid string Peptide if the RNA string transcribed from either Pattern or its reverse complement Pattern translates into Peptide. For example, the DNA string GAAACT is transcribed into GAAACU and translated into ET. The reverse complement of this DNA string, AGTTTC, is transcribed into AGUUUC and translated into SF. Thus, GAAACT encodes both ET and SF.

CODE CHALLENGE: Peptide Encoding Problem.

Peptide Encoding Problem: Find substrings of a genome encoding a given amino acid sequence.
     Input: A DNA string Text, an amino acid string Peptide, and the array GeneticCode.
     Output: All substrings of Text encoding Peptide (if any such substrings exist).

Note: The solution may contain repeated strings if the same string occurs more than once as a substring of Text and encodes Peptide.

Sample Input:

ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA
MA
Sample Output:

ATGGCC
ATGGCC
GGCCAT
'''

def reverse_complement(st):
    s1=st
    i=0
    for i in range (len(s1)):
        if s1[i]=='A':
            s1 = s1[:i] + "T" + s1[i+1:]
            continue
        if s1[i]=='T':
            s1 = s1[:i] + "A" + s1[i+1:]
            continue
        if s1[i]=='G':
            s1 = s1[:i] + "C" + s1[i+1:]
            continue
        if s1[i]=='C':
            s1 = s1[:i] + "G" + s1[i+1:]
            continue
    s1=s1[::-1]
    return str(s1)

def translation1(st):
    s=st
    for i in range (len(s)):
        if s[i]=='T':
            s = s[:i] + "U" + s[i+1:]
            continue
    for i in range (0,len(s),3):
        codon=s[i:i+3]
        if codon=='UAG' :
            s=s[:i] + s[i+3:]
        if codon=='UAA':
            s=s[:i] + s[i+3:]
        if codon=='UGA':
            s=s[:i] + s[i+3:]
    return str(s)

def translation(st):
    s=st
    for i in range (len(s)):
        if s[i]=='T':
            s = s[:i] + "U" + s[i+1:]
            continue
    return str(s)


def retranslation(st):
    s=st
    for i in range (0,len(s),1):
        if s[i]=='U':
            s = s[:i] + "T" + s[i+1:]
            continue
    return str(s)

def reverse(str1):
    str2 = []
    for i in range(len(str1)):
        if str1[i] == 'A':
            str2.append('T')
            continue
        if str1[i] == 'T':
            str2.append('A')
            continue
        if str1[i] == 'C':
            str2.append('G')
            continue
        if str1[i] == 'G':
            str2.append('C')
    result =''.join(str2[::-1])
    return result


def RECURS_CHECK1(s1, s2):
    if CHECK_RNA(s1[0:3])==s2[0]:
        if len(s1) - 1 > 3:
            if RECURS_CHECK1(s1[3:len(s1)], s2[1:len(s2)]) == -1:
                return -1
            else:
                return 1
    else:
        return -1

def RECURS_CHECK2(s1, s2):
    RNA=[['AAA', 'K'], ['AAC', 'N'], ['AAG', 'K'], ['AAT', 'N'], ['ACA', 'T'], ['ACC', 'T'], ['ACG', 'T'],
    ['ACT', 'T'], ['AGA', 'R'], ['AGC', 'S'], ['AGG', 'R'], ['AGT', 'S'], ['ATA', 'I'], ['ATC', 'I'],
    ['ATG', 'M'], ['ATT', 'I'], ['CAA', 'Q'], ['CAC', 'H'], ['CAG', 'Q'], ['CAT', 'H'], ['CCA', 'P'],
    ['CCC', 'P'], ['CCG', 'P'], ['CCT', 'P'], ['CGA', 'R'], ['CGC', 'R'], ['CGG', 'R'], ['CGT', 'R'],
    ['CTA', 'L'], ['CTC', 'L'], ['CTG', 'L'], ['CTT', 'L'], ['GAA', 'E'], ['GAC', 'D'], ['GAG', 'E'],
    ['GAT', 'D'], ['GCA', 'A'], ['GCC', 'A'], ['GCG', 'A'], ['GCT', 'A'], ['GGA', 'G'], ['GGC', 'G'],
    ['GGG', 'G'], ['GGT', 'G'], ['GTA', 'V'], ['GTC', 'V'], ['GTG', 'V'], ['GTT', 'V'], ['TAA', ''],
    ['TAC', 'Y'], ['TAG', ''], ['TAT', 'Y'], ['TCA', 'S'], ['TCC', 'S'], ['TCG', 'S'], ['TCT', 'S'],
    ['TGA', ''], ['TGC', 'C'], ['TGG', 'W'], ['TGT', 'C'], ['TTA', 'L'], ['TTC', 'F'], ['TTG', 'L'],
    ['TTT', 'F']];
    tmp = []
    n = 0
    for i in range(len(RNA)):
        if s2[0] == RNA[i][1]:
            tmp.append(reverse(RNA[i][0]))
            n = n + 1
    for i in range(n):
        if s1[0:3] == tmp[i]:
            if len(s1) - 1 > 3:
                if (RECURS_CHECK2(s1[3:len(s1)], s2[1:len(s2)]) == 1):
                    return 1
            else:
                return 1
    if i == n-1:
        return -1
            
def CHECK_RNA (s1):
    RNA = [['AAA', 'K'], ['AAC', 'N'], ['AAG', 'K'], ['AAT', 'N'], ['ACA', 'T'], ['ACC', 'T'], ['ACG', 'T'],
    ['ACT', 'T'], ['AGA', 'R'], ['AGC', 'S'], ['AGG', 'R'], ['AGT', 'S'], ['ATA', 'I'], ['ATC', 'I'],
    ['ATG', 'M'], ['ATT', 'I'], ['CAA', 'Q'], ['CAC', 'H'], ['CAG', 'Q'], ['CAT', 'H'], ['CCA', 'P'],
    ['CCC', 'P'], ['CCG', 'P'], ['CCT', 'P'], ['CGA', 'R'], ['CGC', 'R'], ['CGG', 'R'], ['CGT', 'R'],
    ['CTA', 'L'], ['CTC', 'L'], ['CTG', 'L'], ['CTT', 'L'], ['GAA', 'E'], ['GAC', 'D'], ['GAG', 'E'],
    ['GAT', 'D'], ['GCA', 'A'], ['GCC', 'A'], ['GCG', 'A'], ['GCT', 'A'], ['GGA', 'G'], ['GGC', 'G'],
    ['GGG', 'G'], ['GGT', 'G'], ['GTA', 'V'], ['GTC', 'V'], ['GTG', 'V'], ['GTT', 'V'], ['TAA', ''],
    ['TAC', 'Y'], ['TAG', ''], ['TAT', 'Y'], ['TCA', 'S'], ['TCC', 'S'], ['TCG', 'S'], ['TCT', 'S'],
    ['TGA', ''], ['TGC', 'C'], ['TGG', 'W'], ['TGT', 'C'], ['TTA', 'L'], ['TTC', 'F'], ['TTG', 'L'],
    ['TTT', 'F']];
    s2 = []
    for i in range(len(RNA)):
           if s1==RNA[i][0]:
                s2.append(RNA[i][1])
                break
    #print('s2',s2)            
    s3 =''.join(s2)
    #print('s3',s3)
    return s3

#######################################################################################################
s1=input()
s2=input()
s3=[]

for i in range(0,len(s1) + 1 - len(s2) * 3,1):
    s3 = RECURS_CHECK1(s1[i:i+len(s2)*3], s2)
    if s3 != -1:
        print(s1[i:i+ len(s2)*3])
    s4 = RECURS_CHECK2(s1[i:i+len(s2)*3], s2[::-1])
    if s4 != -1:
        print(s1[i:i+ len(s2)*3])

