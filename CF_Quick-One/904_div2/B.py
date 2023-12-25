from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N = int(input())
    string = input()
    string = list(string[::-1])
     
    zero_indexes = []
    for i, j in enumerate(string):
        if j == '0':
            zero_indexes.append(i)
    zero_indexes.reverse()

    ANS = []
    moves = 0

    for i in range(N):
        if string[i] == '0':
            ANS.append(moves)
            zero_indexes.pop()
        else:
            if len(zero_indexes) > 0:
                alpha = zero_indexes.pop()
                string[alpha] = '1'
                moves += alpha - i
                ANS.append(moves)
            else:
                break
    
    ANS += [-1] * (N - len(ANS))
    print(*ANS)


    

for _ in range(int(input())):
    solve()