from sys import stdin
def input(): return stdin.readline()[:-1]

arr = [[0] * 1000 for _ in range(1000)]

ANS = []

def reset(n):
    for i in range(n):
        for j in range(n):
            arr[i][j] = 0

def print_arr(n):
    for i in range(n):
        ANS.append(' '.join(map(str, arr[i][:n])))

def solve():
    N, K = map(int, input().split())
    if K%2 == 1:
        ANS.append('No')
        return
    if N == 2:
        ANS.append('Yes')
        if K == 0:
            ANS.append('0 0')
            ANS.append('0 0')
        elif K == 2:
            ANS.append('0 0')
            ANS.append('1 1')
        else:
            ANS.append('1 1')
            ANS.append('1 1')
        return
    
    if K == 2 or K == (N**2-2):
        ANS.append('No')   
        return

    ANS.append('Yes')
    if K%4 == 0:
        alpha= N // 2
        v = K // 4
        for i in range(v):
            r, c = i // alpha, i % alpha
            arr[2*r][2*c] = 1
            arr[2*r+1][2*c] = 1
            arr[2*r][2*c+1] = 1
            arr[2*r+1][2*c+1] = 1
        print_arr(N)
        reset(N)
        return
    else:
        flag = False

        if K >= N**2/2:
            K = N**2 - K
            flag = True
        
        arr[0][0] = 1
        arr[0][1] = 1
        arr[1][0] = 1
        arr[1][2] = 1
        arr[2][1] = 1
        arr[2][2] = 1

        need = (K - 6) // 4
        i = 0

        while need > 0:
            if i == 0 or i == 1 or i == (N//2) or i == (N//2) + 1:
                i += 1
                continue
            r, c = i // (N//2), i % (N//2)
            arr[2*r][2*c] = 1
            arr[2*r+1][2*c] = 1
            arr[2*r][2*c+1] = 1
            arr[2*r+1][2*c+1] = 1
            need -= 1
            i += 1
        

        if flag == True:
            for i in range(N):
                for j in range(N):
                    arr[i][j] = 1 - arr[i][j]
        print_arr(N)
        reset(N)


        
# make array of size 1000x1000
for _ in range(int(input())):
    solve()

import sys
sys.stdout.write('\n'.join(ANS))