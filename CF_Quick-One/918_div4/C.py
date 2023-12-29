from sys import stdin
def input(): return stdin.readline()[:-1]

from math import isqrt

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    s = sum(A)
    q = isqrt(s)
    
    if q * q == s:
        print('YES')
    else:
        print('NO')
    

for _ in range(int(input())):
    solve()