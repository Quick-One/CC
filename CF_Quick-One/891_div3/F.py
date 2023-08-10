from sys import stdin
def input(): return stdin.readline()[:-1]

from collections import Counter
from math import isqrt

def equation_solve(a,b,c):
    Discriminant = b**2 - 4*a*c
    if Discriminant < 0:
        return []
    else:
        x1 = (-b + isqrt(Discriminant)) // (2*a)
        x2 = (-b - isqrt(Discriminant)) // (2*a)
        
        solns = set()
        for x in [x1, x2]:
            if a * x**2 + b * x + c == 0:
                solns.add(x)
        return solns
    



def solve():
    N = int(input())
    arr=  list(map(int, input().split()))
    arr2 = [str(x) for x in arr]
    c = Counter(arr2)
    a = []
    for _ in range(int(input())):
        x, y = map(int, input().split())
        solns = equation_solve(1, -x, y)
        ans = 0
        for s in solns:
            oppo = x - s

            if oppo == s:
                ans += c[str(s)] * (c[str(s)] - 1)
            else:
                ans += c[str(s)] * c[str(oppo)]
        a.append(ans//2)
    print(*a)



for _ in range(int(input())):
    solve()