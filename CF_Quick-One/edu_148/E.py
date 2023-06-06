from sys import stdin
def input(): return stdin.readline()[:-1]

def final_solution(arr):
    x = 0
    for i in range(N):
        x ^= arr[i] * (i + 1)
    print(x)
    exit()

MOD = 998244353
N, a0, x, y, m, k = map(int, input().split())

A = [0] * N
A[0] = a0
for i in range(1, N):
    A[i] = (A[i - 1] * x + y) % m

dp = [[0] * N for _ in range(k + 1)]

dp[0][0] = A[0] % MOD
for i in range(1, N):
    dp[0][i] = (dp[0][i - 1] + A[i]) % MOD


if k == 0: final_solution(dp[0])

dp[1][0] = A[0] % MOD
for j in range(1, N):
    dp[1][j] = (A[j] + dp[1][j - 1] + dp[0][j - 1]) % MOD
for i in range(2, k + 1):
    for j in range(1, N):
        dp[i][j] = (dp[i][j - 1] + dp[i - 1][j - 1]) % MOD
final_solution(dp[k])