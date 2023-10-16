from sys import stdin
def input(): return stdin.readline()[:-1]
 
def ceildiv(a, b):
    return -(a // -b)
 
def solve():
    # N = int(input())
    a,b,c = map(int, input().split())
    d = abs(b-a) /2
    ans = 0
    while d > 0:
        ans += 1
        d -= c
    print(ans)
 
 
 
for _ in range(int(input())):
    solve()