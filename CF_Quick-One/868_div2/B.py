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

def solve():
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    for i in range(N):
        arr[i] -= 1
    # print(arr)
    uf = UnionFind(N)

    for i in range(N):
        neigh = i + K
        if neigh < N:
            uf.union(i, neigh)

    for i in range(N):
        uf.find(i)
    # print(*uf.parent)

    a = defaultdict(set)
    b = defaultdict(set)

    for i in range(N):
        a[uf.parent[i]].add(i)
        b[uf.parent[i]].add(arr[i])
        # print(i, arr[i], uf.parent[i])

    # print(*uf.parent)
    # print(a)
    # print(b)

    d = 0
    k = 0
    for i in a.keys():
        alpha = len(a[i] ^ b[i])

        if alpha == 0:
            continue

        if alpha > 2:
            print(-1)
            return
        
        d += 1
    
    if d == 0:
        print(0)
    elif d == 2:
        print(1)
    else:
        print(-1)


for _ in range(int(input())):
    solve()

