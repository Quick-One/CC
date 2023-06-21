from sys import stdin
def input(): return stdin.readline()[:-1]

from collections import deque
def solve():
    N = int(input())
    s = 0
    while N != 1:
        s += N
        N //= 2
    print(s + 1)
    

for _ in range(int(input())):
    solve()