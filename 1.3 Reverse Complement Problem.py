
'''
CODE CHALLENGE: Reverse Complement Problem.
     Input: A DNA string Pattern.
     Output: Pattern, the reverse complement of Pattern.
Sample Input:

AAAACCCGGT
Sample Output:

ACCGGGTTTT
'''

s=str(input())
s=s[::-1]
i=0
for i in range (len(s)):
    if s[i]=='A':
        s = s[:i] + "T" + s[i+1:]
        continue
    if s[i]=='T':
        s = s[:i] + "A" + s[i+1:]
        continue
    if s[i]=='G':
        s = s[:i] + "C" + s[i+1:]
        continue
    if s[i]=='C':
        s = s[:i] + "G" + s[i+1:]
        continue
print(s)
