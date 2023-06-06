from sys import stdin
def input(): return stdin.readline()[:-1]


MOD = 10**9 + 7

def solve():
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    DP = [[0]*(N+1) for _ in range(64)]
    # DP[i][j] denote   s number of subsequences ending at i with and value j

    for j in range(N):
        e = arr[j]
        j += 1

        for i in range(64):
            # Not considering the current element
            DP[i][j] = DP[i][j-1]
            DP[i][j] %= MOD

            # Considering the current element
            DP[i & e][j] += DP[i][j-1]
            DP[i & e][j] %= MOD

        DP[e][j] += 1
        DP[e][j] %= MOD

    ans = 0
    for i in range(64):
        if bin(i).count("1") == K:
            ans += DP[i][N]
            ans %= MOD
    print(ans)


for _ in range(int(input())):
    solve()
