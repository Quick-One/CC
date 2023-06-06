from sys import stdin
def input(): return stdin.readline()[:-1]

def oi():
    return int(input())
 
def ti():
    return map(int, input().split())
 
def mi():
    return list(map(int, input().split()))

from bisect import bisect_left, bisect_right
from math import sqrt, isqrt

delta = 10 ** -15
def solve():
    N, M = ti()
    slopes = []
    for _ in range(N):
        slopes.append(oi())
    slopes.sort()
    for parabola in range(M):
        a, b, c = ti()
        if c <= 0:
            print('NO')
            continue
        
        k = isqrt(4*a*c)
        if k * k == 4 * a * c:
            lower = b - k + 1
        else:
            lower = b - k
        i1 = bisect_left(slopes, lower)

        if i1 == N:
            print('NO')
        else:
            alp = slopes[i1]
            if (b - alp) ** 2 - 4 * a * c < 0:
                print('YES')
                print(alp)
            else:
                print('NO')






for _ in range(oi()):
    solve()