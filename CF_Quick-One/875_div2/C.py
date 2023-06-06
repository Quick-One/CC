from sys import stdin
def input(): return stdin.readline()[:-1]
from collections import defaultdict, deque

def solve():
    N = int(input())
    g = defaultdict(list)
    
    edges = {}
    for i in range(N-1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append((v, i+1))
        g[v].append((u, i+1))
        edges[min(u, v), max(u, v)] = i+1
    
    answer = [0] * (N)  
    parent = [-1] * (N)
    order = [] 
    bfs_queue = deque()
    bfs_queue.append(0)
    while bfs_queue:
        u = bfs_queue.popleft()
        order.append(u)
        for v, edge in g[u]:
            if v != parent[u]:
                parent[v] = u
                bfs_queue.append(v)
    
    for node in order:
        par = parent[node]
        if node == 0 or par == 0:
            continue
        grandpar = parent[par]

        upper = edges[min(par, grandpar), max(par, grandpar)]
        lower = edges[min(node, par), max(node, par)]

        if upper > lower:
            answer[node] = answer[par] + 1
        else:
            answer[node] = answer[par]
    # print(*answer)
    print(max(answer)+1)

for _ in range(int(input())):
    solve()