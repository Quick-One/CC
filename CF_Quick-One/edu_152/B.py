from sys import stdin
def input(): return stdin.readline()[:-1]

def ceildiv(a, b):
    return -(a // -b)

from collections import defaultdict

def solve():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    d = defaultdict(list)

    for i , j in enumerate(a):
        if j%K == 0:
            d[str(K)].append(i+1)
        else:
            d[str(j%K)].append(i+1)
    
    keys = list(d.keys())
    keys = list(map(int, keys))
    keys.sort()
    ans = []
    # print(d)
    for key in reversed(keys):
        ans.extend(sorted(d[str(key)]))
    print(*ans)

for _ in range(int(input())):
    solve()