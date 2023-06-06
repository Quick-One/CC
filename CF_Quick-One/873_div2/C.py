from sys import stdin
def input(): return stdin.readline()[:-1]

import bisect
MOD = 10**9 + 7
def solve():
    N = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(range(N))
    
    c.reverse()
    a.sort()
    b.sort()

    d = []
    ans = 1

    for i in b:
        index = bisect.bisect_right(a, i)
        greater_than = N - index
        d.append(greater_than)

    e = [d[i] - c[i] for i in range(N)]
    # print(d)
    # print(c)
    # print(e)
    for l in e:
        if l <= 0:
            print(0)
            return
        ans *= l
        ans %= MOD
    print(ans)


for _ in range(int(input())):
    solve()
