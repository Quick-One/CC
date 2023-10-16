from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N, M = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(input().strip())
    
    alpha = []
    for r in A:
        alpha.append(M - r.count('.'))
    for col in range(M):
        alpha.append(N - sum([A[i][col] == '.' for i in range(N)]))
    for i in alpha:
        if i % 2 == 1:
            print(-1)
            return
    
    # ANS (nxm)
    ANS = []
    for i in A:
        ANS.append(list(i))
    for i in range(N):
        next_char = 0
        for j in range(M):
            if A[i][j] == 'U':
                ANS[i][j] = next_char
                ANS[i+1][j] = next_char ^ 1
                next_char ^= 1
    
    for j in range(M):
        next_char = 0
        for i in range(N):
            if A[i][j] == 'L':
                ANS[i][j] = next_char
                ANS[i][j+1] = next_char ^ 1
                next_char ^= 1
    
    # print(ANS)    
    for i in range(N):
        for j in range(M):
            if ANS[i][j] == 0:
                ANS[i][j] = 'W'
            elif ANS[i][j] == 1:
                ANS[i][j] = 'B'
    
    for i in ANS:
        print(''.join(i))

    

    

for _ in range(int(input())):
    solve()