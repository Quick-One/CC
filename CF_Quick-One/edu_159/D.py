from sys import stdin
def input(): return stdin.readline()[:-1]

from collections import defaultdict
from bisect import bisect_left

N, Q = map(int, input().split())
commands = input().strip()

direction = [(0,0)]
d = defaultdict(list)
d[(0,0)].append(0)

x,y = 0,0
for i, c in enumerate(commands):
    if c == 'L': x -= 1
    elif c == 'R': x += 1
    elif c == 'U': y += 1
    elif c == 'D': y -= 1
    direction.append((x,y))
    d[(x,y)].append(i+1)
    
for _ in range(Q):
    x,y,l,r = map(int, input().split())

    if (x,y) in d and (d[(x,y)][0] <= l-1 or d[(x,y)][-1] >= r):
        print('YES')
        continue
    
    start = direction[l-1]
    end = direction[r]

    sx, sy = start
    ex, ey = end
    mx, my = (sx + ex - x), (sy + ey - y)

    if (mx, my) in d:   
        index = bisect_left(d[(mx, my)], l - 1)
        if index < len(d[(mx, my)]) and d[(mx, my)][index] <= r:
            print('YES')
            continue
        
    print('NO')