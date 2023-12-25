from sys import stdin
def input(): return stdin.readline()[:-1]

N, Q = map(int, input().split())
Arr = list(map(int, input().split()))

diffs = [0] * N

def solve(K, Arr):
    for i in range(59, -1, -1):
        power = 1 << i
        needed = 0

        for j in range(N):
            if not (Arr[j] & power):
                diffs[j] = (power - (Arr[j] % power))
            else:
                diffs[j] = 0
        
        s = sum(diffs)
        if K >= s:
            K -= s
            for j in range(N):
                Arr[j] += diffs[j]
    
    ANS = Arr[0]
    for i in range(1, N):
        ANS &= Arr[i]
    return ANS
     
for _ in range(Q):
    q = int(input())
    ans = solve(q, Arr.copy())
    print(ans)