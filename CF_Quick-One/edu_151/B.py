from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    xa, ya = map(int, input().split())
    xb, yb = map(int, input().split())
    xc, yc = map(int, input().split())

    a = [xa, xa, xb, xc]
    b = [ya, ya, yb, yc]

    a.sort()
    b.sort()

    x1, x2 = a[1], a[2]
    y1, y2 = b[1], b[2]

    ANS = abs(x1 - x2) + abs(y1 - y2)
    print(ANS + 1)

for _ in range(int(input())):
    solve()