from sys import stdin
def input(): return stdin.readline()[:-1]

INF = 10**18

N, E = map(int, input().split())
G = [[] for _ in range(N)]

for _ in range(E):
    a, b, w = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append((b, w))
    G[b].append((a, w))

dists = [INF] * N
dists[0] = 0

parent = [-1] * N
parent[0] = 0

from heapq import heappush, heappop
que = [(0, 0)]


while que:
    dist, v = heappop(que)
    if dist > dists[v]:
        continue
    for u, w in G[v]:
        if dists[u] > dists[v] + w:
            dists[u] = dists[v] + w
            parent[u] = v
            heappush(que, (dists[u], u))

if dists[N-1] == INF:
    print(-1)
    exit()

path = [N-1]
while path[-1] != 0:
    path.append(parent[path[-1]])
path = path[::-1]
path = [p+1 for p in path]
print(*path)