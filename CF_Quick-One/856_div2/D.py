from collections import Counter

N = 10 ** 6 + 100
MAX_FAC = 2023
MOD = 998244353

SEIVE = [i for i in range(N + 1)]
SEIVE[1] = 0

for i in SEIVE:
    if i == 0:
        continue
    for j in range(i + i, N + 1, i):
        SEIVE[j] = 0

FACT = [0] * (MAX_FAC+1)
INV_FACT = [0] * (MAX_FAC+1)
FACT[0] = 1

for i in range(1, MAX_FAC+1):
    FACT[i] = (FACT[i-1] * i) % MOD

for i in range(MAX_FAC+1):
    INV_FACT[i] = pow(FACT[i], MOD-2, MOD)


def solve():
    N = int(input())
    A = list(map(int, input().split()))

    PRIMES = []
    COMPOSITE = []

    for i in A:
        if SEIVE[i] == 0:
            COMPOSITE.append(i)
        else:
            PRIMES.append(i)

    C = Counter(sorted(PRIMES))
    C = list(C.items())

    if N > len(C):
        print(0)
        return

    ans = FACT[N]
    for freq in Counter(COMPOSITE).values():
        ans *= INV_FACT[freq]
        ans %= MOD

    p_required = N
    DP = [[0] * (p_required+1) for _ in range(len(C) + 1)]
    DP[0][p_required] = 1

    for r in range(1, len(C) + 1):
        m = INV_FACT[C[r-1][1]]
        DP[r][p_required] = (DP[r-1][p_required] * m) % MOD

    for c in range(p_required-1, -1, -1):
        for r in range(len(C)+1):
            if p_required <= c + r:
                a_i = C[r-1][1]
                term1 = (DP[r-1][c] * INV_FACT[a_i]) % MOD
                term2 = (DP[r-1][c+1] * INV_FACT[a_i-1]) % MOD
                DP[r][c] = (term1 + term2) % MOD

    ans *= DP[len(C)][0]
    ans %= MOD
    print(ans)

solve()
