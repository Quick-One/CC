from sys import stdin
def input(): return stdin.readline()[:-1]

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

from collections import defaultdict, Counter
def solve():
    graph = defaultdict(set)
    N = int(input())
    arr = list(map(int, input().split()))
    arr = [i-1 for i in arr]
    for i, v in enumerate(arr):
        graph[i].add(v)
        graph[v].add(i)

    uf = UnionFind(N)
    for i, v in enumerate(arr):
        uf.union(i, v)
    for i in range(N):
        uf.find(i)

    groups = defaultdict(set)
    group_open = {}

    for i in range(N):
        groups[uf.parent[i]].add(i)
    

    for i,b in groups.items():
        if len(b) > 2:
            group_open[i] = False
            for node in b:
                if len(graph[node]) == 1:
                    group_open[i] = True
                    break
        else:
            group_open[i] = True
    # print(groups)
    # print(group_open)
    
    c = Counter(group_open.values())
    mini = c[False]
    if c[True] > 0:
        mini += 1
    maxi = c[False] + c[True]
    print(mini, maxi)
    


for _ in range(int(input())):
    solve()

