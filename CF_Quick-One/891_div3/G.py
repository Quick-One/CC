from sys import stdin
def input(): return stdin.readline()[:-1]
from collections import defaultdict

MOD = 998244353

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1]*n
    def find(self, a): #return parent of a. a and b are in same set if they have same parent
        acopy = a
        while a != self.parent[a]:
            a = self.parent[a]
        while acopy != a: #path compression
            self.parent[acopy], acopy = a, self.parent[acopy]
        return a
    def union(self, a, b): #union a and b
        self.size[self.find(a)] += self.size[self.find(b)]
        self.parent[self.find(b)] = self.find(a)
    def size_group(self, a):
        return self.size[self.find(a)]

def solve():
    N, S = map(int, input().split())
    edges = []
    for _ in range(N-1):
        u, v, w = map(int, input().split())
        edges.append((w, u-1, v-1))
    edges.sort()
    uf = UnionFind(N)
    ans = 1
    for w, u, v in edges:
        s1 = uf.size_group(u)
        s2 = uf.size_group(v)
        ans *= pow((S - w + 1), s1 * s2 - 1, MOD)
        ans %= MOD
        uf.union(u, v)
    
    print(ans)


for _ in range(int(input())):
    solve()