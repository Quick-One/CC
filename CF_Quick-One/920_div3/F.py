from sys import stdin
def input(): return stdin.readline()[:-1]


def solve():
    N, Q = map(int, input().split())
    Arr = list(map(int, input().split()))
    
    K = int(N ** 0.5) + 1
    
    # MAKE DP OF SIZE N X K
    dp = [[0 for _ in range(N)] for _ in range(K)]
    
    for k in range(1, K):
        for i in range(N-1, -1, -1):
            if i + k < N:
                dp[k][i] = dp[k][i+k] + Arr[i]
            else:
                dp[k][i] = Arr[i]
                
    # making it a suffix
    for k in range(1, K):
        for i in range(N-1, -1, -1):
            if i + k < N:
                dp[k][i] += dp[k][i+k]
    
    ANS = [] 
    for _ in range(Q):
        s, delta, k = map(int, input().split())
        s -= 1
        
        if delta < K:
            temp = 0
            temp += dp[delta][s]
            if s + delta*(k) < N:
                temp -= dp[delta][s+delta*(k)]
                x = dp[delta][s+delta*(k)]
                if (s + delta*(k+1)) < N:
                    x -= dp[delta][s+delta*(k+1)]
                temp -= k * x
            ANS.append(temp)
        else:
            temp = 0
            for i in range(1, k+1):
                temp += Arr[s + (i-1) * delta] * i
            ANS.append(temp)
            
    
    print(*ANS)
for _ in range(int(input())):
    solve()