from sys import stdin
def input(): return stdin.readline()[:-1]

from math import lcm

def solve():
    n, x, y = map(int, input().split())

    total_x = n//x
    total_y = n//y
    common = n//(lcm(x, y))
    total_x -= common
    total_y -= common

    sy = (total_y * (total_y+1))//2
    sx = (n * (n+1)) //2
    k = n-total_x
    sx -= (k * (k+1))//2

    ans = sx - sy
    print(ans)

for _ in range(int(input())):
    solve()