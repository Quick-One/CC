from sys import stdin
def input(): return stdin.readline()[:-1]

from collections import defaultdict
from collections import deque


N = int(input())
A = list(map(int, input().split()))
B = list(range(2, N+1))

g = defaultdict(list)

for i, j in zip(A, B):
    i -= 1
    j -= 1
    g[i].append(j)
    g[j].append(i)

parent = [-1] * N
bfs = deque([0])
order = [0]

while bfs:
    v = bfs.popleft()
    for u in g[v]:
        if u != parent[v]:
            parent[u] = v
            order.append(u)
            bfs.append(u)

dp = [0] * N
for v in reversed(order):
    dp[v] = 1 + sum(dp[u] for u in g[v] if u != parent[v])


def solve(arr):
    dp = [0] * (sum(arr) + 1)
    s = sum(arr)
    dp[0] = 1

    for x in arr:
        for i in range(len(dp) - 1, -1, -1):
            if dp[i]:
                dp[i + x] = 1

    mx = float('-inf')
    for i in range(s + 1):
        if dp[i]: mx = max(mx, i * (s - i))
    
    return mx


ANS = 0

for node in range(N):
    children = []
    for child in g[node]:
        if child != parent[node]:
            children.append(dp[child])
    if len(children)>=2:
        ANS += solve(children)

print(ANS)