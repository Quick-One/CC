from sys import stdin
def input(): return stdin.readline()[:-1]
from collections import defaultdict, deque, Counter

MOD = 10**9+7

def MODINV(x):
    return pow(x, MOD-2, MOD)

N, K = map(int, input().split())

graph = defaultdict(list)
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

if K%2 == 1:
    print(1)
    exit()

visited = [False] * N
parent = [-1] * N
bfs = deque([0])
visited[0] = True
order = []

while bfs:
    now = bfs.popleft()
    order.append(now)
    for next in graph[now]:
        if not visited[next]:
            visited[next] = True
            parent[next] = now
            bfs.append(next)

dp = [0] * N
for node in reversed(order):
    val = 0
    for neigh in graph[node]:
        if neigh != parent[node]:
            val += dp[neigh]
    dp[node] = val + 1


branch_length =[]

num = 0
for node in range(N):
    a = []
    for neigh in graph[node]:
        if neigh != parent[node]:
            a.append(dp[neigh])
    a.append(N - dp[node])
    branch_length.extend(a)

c = Counter(branch_length)
del c[0]


factorial = [1] * (N+1)
for i in range(1, N+1):
    factorial[i] = factorial[i-1] * i % MOD

inv_factorial = [1] * (N+1)
inv_factorial[N] = MODINV(factorial[N])
for i in range(N-1, -1, -1):
    inv_factorial[i] = inv_factorial[i+1] * (i+1) % MOD

def nCr(n, r):
    if n < r:
        return 0
    return factorial[n] * inv_factorial[r] * inv_factorial[n-r] % MOD

first_term = (N) * nCr(N, K) % MOD

second_term = 0
for i in range(1, N//2):
    assert c[i] == c[N-i]
    count = c[i]
    if count == 0:
        continue
    term = nCr(N,K) - (nCr(i, K//2) * nCr(N-i, K//2) % MOD)
    term %= MOD
    term *= count
    term %= MOD
    second_term += term
    second_term %= MOD

count = c[N//2]
if count > 0:
    count //= 2
    term = nCr(N, K) - nCr(N//2, K//2) * nCr(N//2, K//2) % MOD
    term *= count
    term %= MOD
    second_term += term
    second_term %= MOD

numer = (first_term - second_term) % MOD
denom = nCr(N, K)
print(numer * MODINV(denom) % MOD)
