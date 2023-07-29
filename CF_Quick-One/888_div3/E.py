from sys import stdin
import sys
def input(): return stdin.readline()[:-1]


OUT = []
from collections import defaultdict
def topsort(g,vtx):
    degree = [0]*vtx
    for node in g:
        for adjnode in g[node]:
            degree[adjnode]+=1

            
    bfs = [i for i in range(vtx) if degree[i] == 0]
    for node in bfs:
        for adjnode in g[node]:
            degree[adjnode]-=1
            if degree[adjnode] == 0:
                bfs.append(adjnode)
    return bfs


def solve():
    N, K = map(int, input().split())
    C = list(map(int, input().split()))
    free = list(map(int, input().split()))
    free = [i-1 for i in free]
    free = set(free)
    d = defaultdict(list)
    e = defaultdict(list)
    for i in range(N):
        neighs = list(map(int, input().split()))
        for j in neighs[1:]:
            d[j-1].append(i)
            e[i].append(j-1)
    # print(d)
    order = topsort(d,N)
    

    ANS = [0] * N
    for i in order:
        if i in free:
            ANS[i] = 0
        else:
            mix = float('inf') if len(e[i]) == 0 else sum(ANS[j] for j in e[i])
            ANS[i] = min(mix, C[i])
    OUT.append(" ".join(map(str, ANS)))
        
for _ in range(int(input())):
    solve()

sys.stdout.write("\n".join(OUT))