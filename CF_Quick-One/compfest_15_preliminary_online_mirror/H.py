from sys import stdin
def input(): return stdin.readline()[:-1]

N, K = map(int, input().split())
MOD = 998244353

MAX_N = 2 * 10**5 + 10
fact = [1] * MAX_N
divided_fact = [1] * MAX_N
for i in range(1, MAX_N):
    fact[i] = fact[i-1] * i % MOD
for i in range(1, MAX_N):
    divided_fact[i] = pow(fact[i], MOD-2, MOD)

arr = [0] * (K+1)
to_subtract = 0
for i in range(K+1):
    full = fact[i+1] * pow(i+1, K-i, MOD)
    full -= to_subtract
    full %= MOD

    to_subtract += full
    to_subtract %= MOD

    arr[i] = full

ans = 0
for i in range(1, N+1):
    if i > K:
        break
    temp = arr[i] * fact[N] * divided_fact[N-i]
    temp %= MOD
    ans += temp
    ans %= MOD

ans += 1
ans %= MOD
print(ans)