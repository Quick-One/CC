from sys import stdin
def input(): return stdin.readline()[:-1]

def oi():
    return int(input())
 
def ti():
    return map(int, input().split())
 
def mi():
    return list(map(int, input().split()))
 
from collections import defaultdict
def solve():
    N = oi()
    d = defaultdict(int)
    for day in range(1, N+1):
        s = oi()
        arr = mi()
        for i in arr:
            d[i] = max(d[i], day)
    alpha = set(d.values())
    reverse_d = {}

    for key, val in d.items():
        reverse_d[val] = key

    ans = []
    for i in range(1, N+1):
        if i not in alpha:
            print(-1)
            return
        else:
            ans.append(reverse_d[i])
    print(*ans)
for _ in range(oi()):
    solve()