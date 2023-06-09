from sys import stdin, stdout
def input(): return stdin.readline()[:-1]
from collections import defaultdict
from collections import deque

ANS = []
def solve():
    g = defaultdict(list)
    N, M = map(int, input().split())
    for _ in range(M):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)
    
    for root in range(N):

        if len(g[root]) < 4:
            continue

        parent = [-1] * N
        papa = [-1] * N

        for neigh in g[root]:
            if papa[neigh] == -1:
                parent[neigh] = neigh
                papa[neigh] = neigh
                q = deque([neigh]) 
                while q:
                    u = q.popleft()
                    for v in g[u]:
                        if parent[v] == -1 and v != root:
                            parent[v] = u
                            papa[v] = neigh
                            q.append(v)
        d = defaultdict(list)
        for neigh in g[root]:
            d[papa[neigh]].append(neigh)
        cycle = False
        cycle_root = -1
        for neigh in g[root]:
            if len(d[neigh]) >= 2:
                cycle = True
                cycle_root = neigh
                break
        if not cycle:
            continue
        neigh_set = set(g[root])
        # finding the closest neigbour of the cycle root
        closest = -1
        bfs = deque([cycle_root])
        parent = [-1] * N
        parent[cycle_root] = cycle_root
        terminate = False
        # print(d)
        # print(cycle_root+1)
        while bfs:
            if terminate:
                break
            u = bfs.popleft()
            # print(u)
            for v in g[u]:
                # print(v)
                if parent[v] == -1 and v != root:
                    parent[v] = u
                    bfs.append(v)
                    if v in neigh_set:
                        closest = v
                        terminate = True
                        break

        ANS.append("YES")
        TEMP = []
        c = 0
        for neigh in g[root]:
            if neigh != closest and neigh != cycle_root:
                TEMP.append(f'{root+1} {neigh+1}')
                c += 1
                if c == 2:
                    break
        TEMP.append(f'{root+1} {closest+1}')
        TEMP.append(f'{root+1} {cycle_root+1}')
        while parent[closest] != closest:
            TEMP.append(f'{parent[closest]+1} {closest+1}')
            closest = parent[closest]
        ANS.append(str(len(TEMP)))
        ANS.extend(TEMP)
        return



    ANS.append("NO")
            

    

for _ in range(int(input())):
    solve()

stdout.write('\n'.join(ANS))