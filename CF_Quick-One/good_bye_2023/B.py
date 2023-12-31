from sys import stdin
def input(): return stdin.readline()[:-1]

from math import gcd

def func(a,b):
    if a == 1:
        return b * b
    d = gcd(a,b)
    if d == 1:
        return a * b
    a //= d
    b //= d
    ans = d * func(a,b)
    return ans
    

def solve():
    a, b = map(int, input().split())
    print(func(a,b))
    

for _ in range(int(input())):
    solve()