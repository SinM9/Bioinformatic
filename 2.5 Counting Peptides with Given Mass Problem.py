
'''
CODE CHALLENGE:  Counting Peptides with Given Mass Problem.

Counting Peptides with Given Mass Problem: Compute the number of peptides of given mass.
     Input: An integer m.
     Output: The number of linear peptides having integer mass m.

Recall that we assume that peptides are formed from the following 18 amino acid masses:
Image: https://ucarecdn.com/5a3d6f05-f6cb-4971-9745-179b6b2ea1ff/


Sample Input:

1024
Sample Output:

14712706211
'''

from collections import Counter
from math import factorial

def peptideMass(mass, recursive=False):
    amino = ['G', 'A', 'S', 'P', 'V', 'T', 'C', 'L', 'N', 'D', 'Q', 'E', 'M', 'H', 'F', 'R', 'Y', 'W']
    massa = [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
    return recursPeptide(massa, amino, mass, '')


def recursPeptide(massa, amino, mass, peptide):
    if len(massa) == 0 and mass > 0:
        return 0
    elif mass < 0:
        return 0
    elif mass == 0:
        c = Counter(peptide)
        div = 1
        for v in c.values():
            div *= factorial(v)
            
        return factorial(len(peptide))/div
    else:
        return recursPeptide(massa, amino, mass - massa[0], peptide + amino[0]) + \
               recursPeptide(massa[1:], amino[1:], mass, peptide)

Mass = int(input())
print(int(peptideMass(Mass)))
