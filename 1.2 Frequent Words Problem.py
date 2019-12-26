
'''
CODE CHALLENGE: Frequent Words Problem.
     Input: A string Text and an integer k.
     Output: All most frequent k-mers in Text.
Sample Input:

ACGTTGCATGTCGCATGATGCATGAGAGCT
4
Sample Output:

CATG GCAT

'''

s=str(input())
num=int(input())
i=0
j=0
swords = []  # Пустой список
snums = []
unic=0
for j in range(len(s)-num+1):
    if s[j:j+num] not in swords:
        swords.insert(unic,s[j:j+num])
        snums.insert(unic,1)
        unic+=1
    else:
        snums[swords.index(s[j:j+num], 0 ,unic)] = snums[swords.index(s[j:j+num], 0 ,unic)]+1
for i in range (unic-1,-1,-1):
    if(snums[i]==max(snums)):
        print (swords[i])    