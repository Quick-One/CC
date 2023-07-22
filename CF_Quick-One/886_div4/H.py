from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        u, v, w = map(int, input().split())
        u -= 1
        v -= 1
        G[u].append((v, w))
        G[v].append((u, -w))
    
    visited = [False] * N

    for start in range(N):
        if visited[start]:
            continue

        used_coords = set()
        coords = {}
        
        coords[start] = 0
        visited[start] = True

        stack = [start]
        
        while stack:
            node = stack.pop()
            for next, w in G[node]:
                if next in coords:
                    if coords[next] != coords[node] + w:
                        print('NO')
                        return
                else:
                    coords[next] = coords[node] + w
                    used_coords.add(coords[next])
                    stack.append(next)
                    visited[next] = True

    print('YES')


    

for _ in range(int(input())):
    solve()