from sys import stdin
def input(): return stdin.readline()[:-1]

def oi():
    return int(input())
 
def ti():
    return map(int, input().split())
 
def mi():
    return list(map(int, input().split()))
 
def solve():
    r, c, x1 , y1, x2, y2, d = input().split()
    r = int(r)
    c = int(c)
    x = int(x1)
    y = int(y1)
    x2 = int(x2)
    y2 = int(y2)
    d = d.strip()

    if d == 'DL':
        dx = 1
        dy = -1
    elif d == 'DR':
        dx = 1
        dy = 1
    elif d == 'UL':
        dx = -1
        dy = -1
    elif d == 'UR':
        dx = -1
        dy = 1
    
    bounce = 0
    visited = set()
    while True:
        if x == x2 and y == y2:
            print(bounce)
            return

        if (x, y, dx, dy) in visited:
            print(-1)
            return
        
        # print(x, y, dx, dy)
        visited.add((x, y, dx, dy))
        # top right corner bounce
        if x == 1 and y == c and dx == -1 and dy == 1:
            dx = 1
            dy = -1
            bounce += 1
        # top left corner bounce
        elif x == 1 and y == 1 and dx == -1 and dy == -1:
            dx = 1
            dy = 1
            bounce += 1
        # bottom left corner bounce
        elif x == r and y == 1 and dx == 1 and dy == -1:
            dx = -1
            dy = 1
            bounce += 1
        # bottom right corner bounce
        elif x == r and y == c and dx == 1 and dy == 1:
            dx = -1
            dy = -1
            bounce += 1
        # right wall bounce
        elif y == c and dy == 1:
            dy = -1
            bounce += 1
        # left wall bounce
        elif y == 1 and dy == -1:
            dy = 1
            bounce += 1
        # top wall bounce
        elif x == 1 and dx == -1:
            dx = 1
            bounce += 1
        # bottom wall bounce
        elif x == r and dx == 1:
            dx = -1
            bounce += 1
        else:
            x += dx
            y += dy 
       
for _ in range(oi()):
    solve()