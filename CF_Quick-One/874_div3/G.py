from sys import stdin, stdout
def input(): return stdin.readline()[:-1]

from collections import deque, defaultdict

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

ANSWER = []

def solve():
    N = int(input())
    graph = [[] for _ in range(N)]

    edges = {}

    for index in range(N-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        graph[a].append(b)
        graph[b].append(a)
        x,y = min(a,b), max(a,b)
        edges[(x,y)] = index + 1

    if N % 3 != 0:
        ANSWER.append("-1")
        return

    bfs = deque([0])
    visited = [False] * N
    visited[0] = True
    parent = [-1] * N
    order = []
    while bfs:
        v = bfs.popleft()
        order.append(v)
        for u in graph[v]:
            if not visited[u]:
                visited[u] = True
                parent[u] = v
                bfs.append(u)
    
    dp = [1] * N
    for node in reversed(order):
        for child in graph[node]:
            if child != parent[node]:
                dp[node] += dp[child]

    uf = UnionFind(N)
    for node in order:
        if node != 0:
            if dp[node] % 3 != 0:
                uf.union(node, parent[node])
    for node in order:
        uf.find(node)
    
    groups = defaultdict(list)
    for node in range(N):
        groups[uf.parent[node]].append(node)
    
    for group in groups.values():
        if len(group) != 3:
            ANSWER.append("-1")
            return

    ans_edges = set()
    for group in groups.values():
        group_set = set(group)
        for member in group:
            for child in graph[member]:
                if child not in group_set:
                    x,y = min(member, child), max(member, child)
                    ans_edges.add(edges[(x,y)])
    
    ANSWER.append(str(len(ans_edges)))
    ANSWER.append(" ".join(map(str, sorted(ans_edges))))


for _ in range(int(input())):
    solve()

stdout.write("\n".join(ANSWER))