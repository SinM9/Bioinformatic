
'''
CODE CHALLENGE: Pattern Count Problem.
     Input: Two strings, Pattern and Genome.
     Output: Count of appearance of Pattern in Genome.

Sample Input:

ATAT
GATATATGCATATACTT
Sample Output:

3
'''

s1=str(input())
s2=str(input())
num=0
start=0
while start!=-1:
    start= s2.find(s1, start, len(s2))
    if(start!=-1):
        num+=1
        start+=1
print(num)