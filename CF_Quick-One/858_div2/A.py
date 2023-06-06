from sys import stdin
def input(): return stdin.readline()[:-1]

def oi():
    return int(input())
 
def ti():
    return map(int, input().split())
 
def mi():
    return list(map(int, input().split()))
 
def solve():
    x1, y1, x2, y2 = ti()
    d = y2 - y1
    l = x1 - x2 + d

    if d >= 0 and l >= 0:
        print(d + l)
    else:
        print(-1)
    
for _ in range(oi()):
    solve()