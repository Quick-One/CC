from sys import stdin
def input(): return stdin.readline()[:-1]
 
from collections import defaultdict
 
from random import getrandbits

RANDOM = getrandbits(32)

class Wrapper(int):
    def __init__(self, x):
        int.__init__(x)
    def __hash__(self):
        return super(Wrapper, self).__hash__() ^ RANDOM


def solve():
    N = int(input())
 
    points = []
    for _ in range(N):
        a,b = map(int, input().split())
        points.append((a,b))
 
    ans = 0
    dx = defaultdict(list)
    dy = defaultdict(list)
    for a,b in points:
        dx[Wrapper(a)].append(b)
        dy[Wrapper(b)].append(a)
    
    for k in dx:
        size = len(dx[k])
        ans += size*(size-1)
    
    for k in dy:
        size = len(dy[k])
        ans += size*(size-1)
    
    rotated_points = [(x+y, x-y) for x,y in points]
    dx = defaultdict(list)
    dy = defaultdict(list)
 
    for a, b in rotated_points:
        dx[Wrapper(a)].append(b)
        dy[Wrapper(b)].append(a)
    
    for k in dx:
        size = len(dx[k])
        ans += size*(size-1)
    
    for k in dy:
        size = len(dy[k])
        ans += size*(size-1)
    
    print(ans)
 
for _ in range(int(input())):
    solve()