from sys import stdin
def input(): return stdin.readline()[:-1]

from collections import deque
def find_cycle(g, N):
    degree_1 = []
    g_copy = [i.copy() for i in g]

    for i in range(N):
        if len(g_copy[i]) == 1:
            degree_1.append(i)

    while degree_1:
        node = degree_1.pop()
        if len(g_copy[node]) == 1:
            next_node = g_copy[node].pop()
            g_copy[next_node].remove(node)
            if len(g_copy[next_node]) == 1:
                degree_1.append(next_node)
    

    start = None
    for i in range(N):
        if len(g_copy[i]) > 1:
            start = i
            break
    
    dfs_stack = []
    dfs_stack.append(start)
    cycle = []
    visited = set()

    while dfs_stack:
        node = dfs_stack.pop()
        if node in visited:
            continue
        visited.add(node)
        cycle.append(node)
        for i in g_copy[node]:
            dfs_stack.append(i)
    
    return cycle

def solve():
    N, A, B = map(int, input().split())
    g = [set() for _ in range(N+1)]
    
    A -= 1
    B -= 1

    for _ in range(N):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        g[x].add(y)
        g[y].add(x)
    
    cycle = find_cycle(g, N)
    
    LEVEL = [-1] * (N)
    group_leader = [-1] * (N)

    for i in cycle:
        LEVEL[i] = 0
        group_leader[i] = i

    for i in cycle:
        start = i
        bfs = deque([start])
        while bfs:
            node = bfs.popleft()
            for j in g[node]:
                if LEVEL[j] == -1:
                    LEVEL[j] = LEVEL[node] + 1
                    group_leader[j] = start
                    bfs.append(j)
    # print(cycle)
    # FInal ans
    level_A = LEVEL[A]
    level_B = LEVEL[B]
    # print(group_leader)
    # print(LEVEL)
    ga , gb  = group_leader[A], group_leader[B]
    i1, i2 = cycle.index(ga), cycle.index(gb)
    dist = abs(i1 - i2)
    dist = min(dist, len(cycle) - dist)
    # print(cycle, ga, gb, i1, i2, dist)

    # print(level_A, level_B, dist)
    if ( A== B):
        print("NO")
        return

    if B in cycle:
        print("YES")
        return


    if dist + level_A > level_B:
        print("YES")
    else:
        print("NO") 


for _ in range(int(input())):
    solve()