
'''
CODE CHALLENGE: Use OUTPUTLCS to solve the Longest Common Subsequence Problem.
     Input: Two strings s and t.
     Output: A longest common subsequence of s and t.

(Note: more than one solution may exist, in which case you may output any one.)


Sample Input:

AACCTTGG
ACACTGTGA
Sample Output:

AACTTG

'''
def BackTrack(str1, str2):
    Mat = [[0] * (len(str2) + 1) for i in range(len(str1) + 1)]
    s = ''

    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i-1] == str2[j-1]:
                Mat[i][j] = Mat[i-1][j-1] + 1						
            else:
                if Mat[i-1][j] >= Mat[i][j-1]:
                    Mat[i][j] = Mat[i-1][j]
                else:
                    Mat[i][j] = Mat[i][j-1]

    t = Mat[len(str1)][len(str2)]
    for i in range(len(str1)):
        for j in range(len(str2)):
            if (str1[len(str1) - i - 1] == str2[len(str2) - j - 1]) & (Mat[len(str1) - i][len(str2) - j] == t):
                s += str1[len(str1) - i - 1]
                t -= 1
                break
    res = ''            
    for i in range(len(s)):
	    res += s[len(s) - i - 1]
    return res    
################                
str1 = str(input())	
str2 = str(input())			
print(BackTrack(str2, str1))