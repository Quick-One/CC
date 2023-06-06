from sys import stdin
def input(): return stdin.readline()[:-1]

def oi():
    return int(input())
 
def ti():
    return map(int, input().split())
 
def mi():
    return list(map(int, input().split()))

def ceildiv(a, b):
    return -(a // -b)

def cost(a,b,m):
    return ceildiv(a,m) + ceildiv(b,m) + m - 1 

from math import sqrt
def solve():
    a,b = ti()
    c = int(sqrt(a+b))

    lower = max(1, c - 10**4)
    upper = c + 10**4

    ans = float('inf')
    for i in range(lower, upper+1):
        ans = min(ans, cost(a,b,i))
    print(ans)

    
for _ in range(oi()):
    solve()