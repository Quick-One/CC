from sys import stdin
def input(): return stdin.readline()[:-1]

def ceildiv(a, b):
    return -(a // -b)

def solve():
    N = int(input())
    a = []
    for _ in range(N):
        c,d = map(int, input().split())
        a.append((c,d))
    ans = float('inf')
    for d,s in a:
        ans = min(ans, (2*d-1+s)//2)
    print(ans)


for _ in range(int(input())):
    solve()