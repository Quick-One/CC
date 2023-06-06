from sys import stdin
def input(): return stdin.readline()[:-1]
from math import lcm, gcd
def solve():
    N = int(input())
    a = []
    b = []
    for _ in range(N):
        x,y = map(int, input().split())
        a.append(x)
        b.append(y)

    intervals = 1
    g = a[0]*b[0]
    l = b[0]
    for i in range(1, N):
        if gcd(g, a[i]*b[i]) % lcm(l, b[i]) == 0:
            g = gcd(g, a[i]*b[i])
            l = lcm(l, b[i])
        else:
            intervals += 1
            g = a[i]*b[i]
            l = b[i]
    print(intervals)

for _ in range(int(input())):
    solve()