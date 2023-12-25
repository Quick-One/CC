from sys import stdin
def input(): return stdin.readline()[:-1]

from collections import deque

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    children = [[] for _ in range(N)]

    for i in range(N - 1):
        children[A[i] - 1].append(i + 1)

    bfs = deque([0])
    order = []

    while bfs:
        v = bfs.popleft()
        order.append(v)
        for u in children[v]:
            bfs.append(u)

    size = [1] * N
    for node in reversed(order):
        size[node] += sum(size[child] for child in children[node])

    dp = [0] * N
    for node in reversed(order):
        
        child_index, mx = -1, -1
        for child in children[node]:
            if size[child] > mx:
                mx = size[child]
                child_index = child

        if child_index == -1:
            dp[node] = 1
            continue

        if (2 * mx) <= (size[node] - 1):
            dp[node] = (size[node] - 1)%2 + 1
            continue
    
        dp[node] = max(0, dp[child_index] - (size[node] - 1 - mx)) + 1

    print((N - dp[0])//2)

for _ in range(int(input())):
    solve()