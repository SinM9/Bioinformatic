
'''
CODE CHALLENGE: Protein Translation Problem.

Protein Translation Problem: Translate an RNA string into an amino acid string using RNA Codon Table.
     Input: An RNA string Pattern.
     Output: The translation of Pattern into an amino acid string Peptide.

Download RNA Codon Table

Sample Input:

AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA
Sample Output:

MAMAPRTEINSTRING
'''

s=str(input())
result=""
RNA={
'AAA':'K', 'AAC':'N', 'AAG':'K', 'AAU':'N','ACA': 'T', 'ACC':'T', 'ACG':'T', 'ACU':'T', 'AGA':'R', 'AGC': 'S','AGG': 'R','AGU': 'S','AUA': 'I','AUC': 'I','AUG': 'M','AUU': 'I','CAA': 'Q','CAC': 'H','CAG': 'Q','CAU': 'H','CCA': 'P','CCC': 'P','CCG': 'P','CCU': 'P','CGA': 'R','CGC': 'R','CGG': 'R','CGU': 'R','CUA': 'L','CUC': 'L','CUG': 'L','CUU': 'L','GAA': 'E','GAC': 'D','GAG': 'E','GAU': 'D','GCA': 'A','GCC': 'A','GCG': 'A','GCU': 'A', 'GGA': 'G','GGC': 'G','GGG': 'G','GGU': 'G','GUA': 'V','GUC': 'V','GUG': 'V','GUU': 'V','UAA':'','UAC': 'Y','UAG':'','UAU': 'Y','UCA': 'S','UCC': 'S','UCG':'S','UCU':'S','UGA':'', 'UGC': 'C','UGG': 'W','UGU': 'C','UUA':'L', 'UUC':'F', 'UUG':'L', 'UUU':'F'
}
    
i=0
codon=''
for i in range(0,len(s),3):
    codon=s[i:i+3]
    result+=RNA[codon]
print (result) 
