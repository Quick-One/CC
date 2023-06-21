from sys import stdin
def input(): return stdin.readline()[:-1]

from collections import deque
def solve():
    N = int(input())
    Arr = list(map(int, input().split()))

    Arr.sort()
    Arr = deque(Arr)
    ans = 0
    while len(Arr) >= 2:
        l = Arr.popleft()
        r = Arr.pop()
        ans += l - r

    print(-ans)


for _ in range(int(input())):
    solve()