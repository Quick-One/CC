from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    n, m, k = map(int, input().split())
    k += 1 
    MAP = [[0] * m for _ in range(n)]
    
    for i in range(n):
        string = input().strip()
        for j in range(m):
            if string[j] == '#':
                MAP[i][j] = 1
                
    for i in range(n):
        for j in range(m):
            if i > 0:
                MAP[i][j] += MAP[i-1][j]
            if j > 0:
                MAP[i][j] += MAP[i][j-1]
            if i > 0 and j > 0:
                MAP[i][j] -= MAP[i-1][j-1]

    
    def area_sum(tlx, tly, brx, bry):
        res = MAP[brx][bry]
        if tly > 0:
            res -= MAP[brx][tly-1]
        if tlx > 0:
            res -= MAP[tlx-1][bry]
        if tly > 0 and tlx > 0:
            res += MAP[tlx-1][tly-1]
        return res
    
    x = k
    A = []
    while x > 0:
        A.append(x)
        x >>= 1
    A.reverse()
    
    DP = [[[0] * len(A) for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            DP[i][j][0] = area_sum(i, j, i, j)
    
    
    ANS = -1
    
    # NORTH WEST DIRECTION
    for k in range(1, len(A)):
        block = A[k] - A[k-1]
        for i in range(n):
            for j in range(m):
                DP[i][j][k] = 0
                if i - block >= 0:
                    DP[i][j][k] += DP[i-block][j][k-1]
                if j + block<= m-1:
                    DP[i][j][k] += DP[i][j+block][k-1]
                tlx, tly = max(i - block + 1, 0), j
                brx, bry = i, min(j + block - 1, m-1)
                DP[i][j][k] += area_sum(tlx, tly, brx, bry)
                
    for i in range(n):
        for j in range(m):
            ANS = max(ANS, DP[i][j][len(A)-1])
    
    # NORTH EAST DIRECTION
    for k in range(1, len(A)):
        block = A[k] - A[k-1]
        for i in range(n):
            for j in range(m):
                DP[i][j][k] = 0
                if i - block >= 0:
                    DP[i][j][k] += DP[i-block][j][k-1]
                if 0<= j - block:
                    DP[i][j][k] += DP[i][j-block][k-1]
                tlx, tly = max(i - block + 1, 0), max(j - block + 1, 0)
                brx, bry = i, j
                DP[i][j][k] += area_sum(tlx, tly, brx, bry)
                
    for i in range(n):
        for j in range(m):
            ANS = max(ANS, DP[i][j][len(A)-1])
    
    # SOUTH WEST DIRECTION
    for k in range(1, len(A)):
        block = A[k] - A[k-1]
        for i in range(n):
            for j in range(m):
                DP[i][j][k] = 0
                if i + block <= n-1:
                    DP[i][j][k] += DP[i+block][j][k-1]
                if j + block <= m-1:
                    DP[i][j][k] += DP[i][j+block][k-1]
                tlx, tly = i, j
                brx, bry = min(n-1, i + block - 1), min(j + block - 1, m-1)
                DP[i][j][k] += area_sum(tlx, tly, brx, bry)
                
    for i in range(n):
        for j in range(m):
            ANS = max(ANS, DP[i][j][len(A)-1])
    
    # SOUTH EAST DIRECTION
    for k in range(1, len(A)):
        block = A[k] - A[k-1]
        for i in range(n):
            for j in range(m):
                DP[i][j][k] = 0
                if i + block <= n-1:
                    DP[i][j][k] += DP[i+block][j][k-1]
                if j - block >= 0:
                    DP[i][j][k] += DP[i][j-block][k-1]
                tlx, tly = i, max(j - block + 1, 0)
                brx, bry = min(i + block - 1, n-1), j
                DP[i][j][k] += area_sum(tlx, tly, brx, bry)
                
    for i in range(n):
        for j in range(m):
            ANS = max(ANS, DP[i][j][len(A)-1])
            
    print(ANS)
    


for _ in range(int(input())):
    solve()