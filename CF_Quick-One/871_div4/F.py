from sys import stdin
def input(): return stdin.readline()[:-1]

from collections import defaultdict, Counter

def solve():
    n, m = map(int, input().split())
    degree = defaultdict(int)

    for _ in range(m):
        u, v = map(int, input().split())
        degree[u] += 1
        degree[v] += 1
    
    c = Counter(degree.values())
    if 1 in c.values():
        prod = c[1]
        for a,b in c.items():
            if b == 1:
                x = a
        y = prod//x
        print(x,y)
    else:
        prod = c[1]
        for a,b in c.items():
            if a != 1:
                x = a
        y = prod//x
        print(x,y)

for _ in range(int(input())):
    solve()