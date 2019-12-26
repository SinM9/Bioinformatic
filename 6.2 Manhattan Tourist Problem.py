
'''
CODE CHALLENGE: Find the length of a longest path in the Manhattan Tourist Problem.
     Input: Integers n and m, followed by an n × (m + 1) matrix Down and an (n + 1) × m matrix Right.
     The two matrices are separated by the - symbol.
     Output: The length of a longest path from source (0, 0) to sink (n, m) in the n × m rectangular grid
     whose edges are defined by the matrices Down and Right.


Sample Input:

5 9
4 1 2 3 1 0 3 0 1 2
3 0 3 2 4 3 2 3 0 2
3 2 2 2 2 3 0 1 0 3
3 0 4 4 2 4 2 0 2 1
1 4 3 1 1 0 2 0 4 0
-
2 3 3 4 3 0 1 2 2
0 3 2 2 4 4 0 2 1
3 3 2 1 3 4 2 0 4
2 0 1 2 1 3 4 2 0
4 3 3 4 1 4 1 3 2
4 3 0 4 2 3 3 3 2
Sample Output:

42
'''

def ManhattanTouristProblem(n, m, down, right):
    score = [[0] * (m+1) for i in range(n+1)]
    for i in range(1,m+1):
        score[0][i] = score[0][i-1] + int(right[0][i-1])
    for j in range(1,n+1):
        score[j][0] = score[j-1][0] + int(down[j-1][0])
    for i in range(1,n+1):
        for j in range(1,m+1):
            score[i][j] = max(score[i-1][j] + int(down[i-1][j]), score[i][j-1] + int(right[i][j-1]))
    return score[n][m]

n, m = map(int, input().split(' '))
down = []
right = []
flag = 0
while (1):
    try:
        i=str(input()).replace(' ', '')
        if (i != '-')&(flag == 0):
            down.append(i)
        else:
            flag = 1
            if i != '-':
                right.append(i)
    except EOFError:
        break
print(ManhattanTouristProblem(n, m, down, right))