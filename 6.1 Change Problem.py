
'''
CODE CHALLENGE: Solve the Change Problem.
     Input: An integer money and an array Coins = (coin1, ..., coind).
     Output: The minimum number of coins with denominations Coins that changes money.


Sample Input:

40
50,25,20,10,5,1
Sample Output:

2
'''
def ChangeProblem(Coins, money):
    result = []
    for i in Coins:
        if money % i == 0:
            result.append(int(money / i))
            break
    C = {}
    while (money != 0):
        C[max(Coins)] = money // max(Coins)
        money = money % max(Coins)
        Coins.remove(max(Coins))
    result.append(sum(C.values()))
    #print(C.values(),sum(C.values()))
    return int(min(result))
##############################################

money=int(input())
Coins=list(map(int,input().split(',')))
print(ChangeProblem(Coins, money))
