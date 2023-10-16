from sys import stdin
def input(): return stdin.readline()

n, a, b, c = map(int, input().split())

dp = [-1] *( n + 1)
dp[0] = 0
for increment in [a,b,c]:
    for i in range(0, n+1):
        if dp[i] != -1 and i + increment <= n:
            dp[i + increment] = max(dp[i + increment], dp[i] + 1)
print(dp[n])
