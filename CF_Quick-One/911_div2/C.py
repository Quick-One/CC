from sys import stdin
def input(): return stdin.readline()[:-1]

INF = 10**18

from collections import deque

def solve():
    N = int(input())
    string = input().strip()
    g = []
    for i in range(N):
        a,b = map(int, input().split())
        a -= 1
        b -= 1
        g.append((a,b))
    
    bfs = deque([0])

    order = []
    while bfs:
        node  = bfs.popleft()
        order.append(node)
        for next_node in g[node]:
            if next_node != -1:
                bfs.append(next_node)

    # print(order)
    dp = [INF] * (N)

    for node in reversed(order):
        if g[node][0] == -1 and g[node][1] == -1:
            # leaf node
            dp[node] = 0
            continue

        l, r = INF, INF

        if g[node][0] != -1:
            l = dp[g[node][0]]
            if string[node] != 'L':
                l += 1
        
        if g[node][1] != -1:
            r = dp[g[node][1]]
            if string[node] != 'R':
                r += 1

        dp[node] = min(l, r)
        
    print(dp[0])
for _ in range(int(input())):
    solve()