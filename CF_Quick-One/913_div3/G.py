from sys import stdin
def input(): return stdin.readline()[:-1]

from collections import defaultdict

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    def find(self, a): #return parent of a. a and b are in same set if they have same parent
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a: #path compression
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a
    def union(self, a, b): #union a and b
        self.parent[self.find(b)] = self.find(a)


def get_ans(arr, color, g):
    paths = []
    temp = []

    for i in arr:
        if color[i] == 1:
            if len(temp) == 0:
                temp.append(i)
            else:
                temp.append(i)
                paths.append(temp)
                temp = []
        else:
            if len(temp) == 0:
                pass
            else:
                temp.append(i)
    ans = set()
    for p in paths:
        for i in range(len(p) - 1):
            ans.add(g[p[i]][p[i+1]] + 1)
    return ans


def solve():
    N = int(input())
    color = list(map(int, input()))

    e = list(map(int, input().split()))
    e = [x - 1 for x in e]


    uf = UnionFind(N)

    g = [dict() for _ in range(N)]
    for i in range(N):
        x,y = i, e[i]
        if x in g[y]: continue
        g[x][y] = x
        g[y][x] = x
        uf.union(x,y)

    for i in range(N):
        uf.find(i)
    
    groups = defaultdict(list)
    for i in range(N):
        groups[uf.parent[i]].append(i)


    visited = [False] * N

    for group in groups.values():
        BLACK = 0
        for i in group:
            if color[i] == 1:
                BLACK += 1
        if BLACK % 2 != 0:
            print(-1)
            return

    ANS = set()

    for group in groups.values():
        leaves = []
        for i in group:
            if len(g[i]) == 1:
                leaves.append(i)

        while leaves:
            node = leaves.pop()
            visited[node] = True

            if len(g[node]) == 0:
                continue
            par = next(iter(g[node]))

            if color[node] == 1:
                ANS.add(g[node][par] + 1)
                color[node] ^= 1
                color[par] ^= 1

            del g[node][par]
            del g[par][node]
            if len(g[par]) == 1:
                leaves.append(par)

        cycle_start = None
        for i in group:
            if not visited[i] and color[i] == 1:
                cycle_start = i
                break
        if cycle_start is None:
            continue
        
        order = []
        dfs = [cycle_start]
        visited[cycle_start] = True
        while dfs:
            node = dfs.pop()
            order.append(node)
            for nei in g[node]:
                if not visited[nei]:
                    visited[nei] = True
                    dfs.append(nei)

        possible1 = order
        possible2 = order[1:] + order[:1]
        ans1 = get_ans(possible1, color, g)
        ans2 = get_ans(possible2, color, g)

        if len(ans1) < len(ans2):
            ANS.update(ans1)
        else:
            ANS.update(ans2)

    print(len(ANS))
    print(*ANS)


for _ in range(int(input())):
    solve() 