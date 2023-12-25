from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    p, q, sx, sy, d = map(int, input().split())
    ANS = p + q - 2

    x = sx + d 
    y = sy + d 
    x0 = sx - d
    y0 = sy - d
    if not (p > x or q > y) or  not (x0 > 1 or y0 > 1) or (x0<=1 and x>=p) or (y0<=1 and y>=q):
        print(-1)
    else:
        print(ANS)
       

for _ in range(int(input())):
    solve()