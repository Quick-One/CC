from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    x4, y4 = map(int, input().split())
    
    xm = min(x1, x2, x3, x4)
    xM = max(x1, x2, x3, x4)
    ym = min(y1, y2, y3, y4)
    yM = max(y1, y2, y3, y4)
    
    print((xM - xm ) * (yM - ym))

for _ in range(int(input())):
    solve()