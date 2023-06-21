from sys import stdin
import sys
def input(): return stdin.readline()[:-1]
ans = []
from collections import deque, defaultdict
def solve():
    N = int(input())
    graph = defaultdict(list)

    for _ in range(N-1):
        a,b = map(int, input().split())
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)
    
    bfs = deque([0])
    visited = [False] * N
    parent = [-1] * N
    visited[0] = True
    order = []
    while bfs:
        node = bfs.popleft()
        order.append(node)
        for child in graph[node]:
            if not visited[child]:
                visited[child] = True
                parent[child] = node
                bfs.append(child)

    dp = [0] * N
    for node in reversed(order):
        if len(graph[node]) == 1 and node != 0:
            dp[node] = 1
        else:
            for child in graph[node]:
                if child != parent[node]:
                    dp[node] += dp[child]
    for _ in range(int(input())):
        a,b = map(int, input().split())
        a -= 1
        b -= 1
        ans.append(dp[a] * dp[b])



    

for _ in range(int(input())):
    solve()

sys.stdout.write('\n'.join(map(str, ans)))