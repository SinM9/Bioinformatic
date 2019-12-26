
'''
Edit Distance Problem: Find the edit distance between two strings.
     Input: Two strings.
     Output: The edit distance between these strings.

CODE CHALLENGE: Solve the Edit Distance Problem.


Sample Input:

PLEASANTLY
MEANLY
Sample Output:

5
'''

str1 = str(input())
str2 = str(input())
M=[[]]
M = [[0 for j in range(len(str2) + 1)] for i in range(len(str1)+1)]
for i in range(1, len(str1) + 1):
	M[i][0] = i 
for j in range(1, len(str2) + 1):
	M[0][j] = j

for i in range(1, len(str1) + 1):
	for j in range (1, len(str2) + 1):
		if str1[i-1] == str2[j-1]:
			M[i][j] = M[i-1][j-1]
		else:
			M[i][j] = min(M[i-1][j] +1, M[i][j-1] + 1, M[i-1][j-1] + 1)
print(M[len(str1)][len(str2)])