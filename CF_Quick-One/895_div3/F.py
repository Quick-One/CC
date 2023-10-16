from sys import stdin
def input(): return stdin.readline()[:-1]

from collections import deque

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
    N = int(input())
    parent = list(map(int, input().split()))
    parent = [x-1 for x in parent]
    cost = list(map(int, input().split()))

    uf = UnionFind(N)
    for i in range(N):
        uf.union(i, parent[i])
    for i in range(N):
        uf.find(i)
    ANS = []
    groups = {}
    for i in range(N):
        if uf.parent[i] not in groups:
            groups[uf.parent[i]] = []
        groups[uf.parent[i]].append(i)
    
    # each group has a cycle
    # idenify the member of cycle

    for group in groups:
        members = groups[group]
        visited = set()
        cycle = set()
        mem = members[0]
        curr = mem
        while curr not in visited:
            visited.add(curr)
            curr = parent[curr]
        
        # cur is a member of cycle
        # find the cycle
        start = curr
        cycle.add(curr)
        curr = parent[curr]
        while curr != start:
            cycle.add(curr)
            curr = parent[curr]
        
        ans_queue = deque()
        done = set()
        for m in members:
            if m in done:
                continue
            if m in cycle:
                continue
            temp = []
            curr = m
            while (curr not in cycle) and (curr not in done):
                temp.append(curr)
                done.add(curr)
                curr = parent[curr]
            
            for i in reversed(temp):
                ans_queue.appendleft(i)

        mini = min(cycle, key=lambda x: cost[x])
            ## add mini at the end
            ## add other memebers of the cycle first

        start = parent[mini]
        while start != mini:
            ans_queue.append(start)
            start = parent[start]
        ans_queue.append(mini)
        ANS.extend(ans_queue)
    ANS = [x+1 for x in ANS]
    print(*ANS)
            




for _ in range(int(input())):
    solve()