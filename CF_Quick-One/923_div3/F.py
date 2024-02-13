from copy import deepcopy
from collections import deque
from sys import stdin
def input(): return stdin.readline()[:-1]


def find_bridges(graph):
    g = deepcopy(graph)
    n = len(g)
    visited = [False]*n
    timer = 0
    parent = [-1]*n
    tin = [0]*n
    low = [0]*n
    look_for = [-1]*n

    bridges = set()

    stack = []
    for node in range(n):
        if visited[node]:
            continue
        stack.append(node)
        while stack:
            x = stack[-1]

            if not visited[x]:
                visited[x] = True
                tin[x] = low[x] = timer
                timer += 1

            else:
                if len(g[x]) == 0:
                    stack.pop()

                else:
                    y = g[x].pop()
                    if y == parent[x]:
                        continue

                    elif y == look_for[x]:
                        look_for[x] = -1
                        low[x] = min(low[x], low[y])
                        if (low[y] > tin[x]):
                            bridges.add((min(x, y), max(x, y)))

                    elif visited[y]:
                        low[x] = min(low[x], tin[y])

                    else:
                        look_for[x] = y
                        stack.append(y)
                        g[x].append(y)
                        parent[y] = x

    return bridges


def solve():
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        edges.append((c, a-1, b-1))
    edges.sort()

    g = [[] for _ in range(n)]
    for _, a, b in edges:
        g[a].append(b)
        g[b].append(a)

    bridges = find_bridges(g)
    for i in range(m):
        COST, x, y = edges[i]
        if (min(x, y), max(x, y)) not in bridges:
            break


    bfs = deque([x])
    parent = [None]*n
    parent[x] = -1

    while bfs:
        node = bfs.popleft()
        if node == y:
            break
        for child in g[node]:
            if node == x and child == y:
                continue
            
            if parent[child] is None:
                parent[child] = node
                bfs.append(child)

    cycle = [y]
    while cycle[-1] != x:
        cycle.append(parent[cycle[-1]])

    print(COST, len(cycle))
    print(*[x+1 for x in cycle])


for _ in range(int(input())):
    solve()
