from sys import stdin
def input(): return stdin.readline()[:-1]

from heapq import heappush, heappop

# make array of size 1000 x 1001
DP = [[float('inf')] * 1001 for _ in range(1000)]

def solve():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    
    start = 0
    end = N-1
    
    for _ in range(M):
        u, v, w = map(int, input().split())
        graph[u-1].append((v-1, w))
        graph[v-1].append((u-1, w))
    
    cost = list(map(int, input().split()))
    
    DP[start][cost[start]] = 0
    heap = [(0, start, cost[start])]
    while heap:
        d, node, c = heappop(heap)
        if DP[node][c] < d:
            continue
        
        for v, w in graph[node]:
            x = min(c, cost[v])
            if DP[v][x] > d + w * c:
                DP[v][x] = d + w * c
                heappush(heap, (DP[v][x], v, x))            
    
    ANS = float('inf')
    for i in range(1, 1001):
        ANS = min(ANS, DP[end][i])
    print(ANS)
    
    for i in range(N):
        for j in range(1, 1001):
            DP[i][j] = float('inf')
    
            

for _ in range(int(input())):
    solve()