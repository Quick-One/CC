from sys import stdin
def input(): return stdin.readline()[:-1]

INF = 10 ** 18

from heapq import heappush, heappop

def solve():
    N, M = map(int, input().split())
    start = int(input(), 2)

    A = []
    for _ in range(M):
        time = int(input())
        cure = int(input(), 2)
        side_effect = int(input(), 2)
        A.append((time, cure, side_effect))
    
    total_states = 2 ** N

    distance = [INF] * total_states
    distance[start] = 0

    heap = [(0, start)]

    while heap:
        d, u = heappop(heap)
        if d > distance[u]:
            continue
            
        for time, cure, side_effect in A:
            next_node = (u & ~cure) | side_effect

            if distance[next_node] > distance[u] + time:
                distance[next_node] = distance[u] + time
                heappush(heap, (distance[next_node], next_node))
            
    if distance[0] == INF:
        print(-1)
    
    else:
        print(distance[0])


    


for _ in range(int(input())):
    solve()