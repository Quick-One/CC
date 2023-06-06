def oi():
    return int(input())
 
def ti():
    return map(int, input().split())
 
def mi():
    return list(map(int, input().split()))
 
def solve():
    n, m= ti()
    pad = len(bin(m)[2:])
    print(n*m)
    for r in range(n):
        for c in range(m):
            print(c + (r<<pad), end=' ')
        print()

for _ in range(oi()):
    solve()