from sys import stdin
def input(): return stdin.readline()[:-1]

from collections import deque
def solve():
    N = int(input())
    Arr = list(map(int, input().split()))

    s = 0
    for i in Arr:
        s += abs(i)

    d = []
    for i in Arr:
        if i != 0:
            d.append(i//abs(i))
    e = []
    for i in d:
        if len(e) == 0:
            e.append(i)
        else:
            if e[-1] == i:
                continue
            else:
                e.append(i)

    # print(d)
    print(s, e.count(-1))

for _ in range(int(input())):
    solve()