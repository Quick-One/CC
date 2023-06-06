from sys import stdin
def input(): return stdin.readline()[:-1]
from math import gcd
def solve():
    N = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    for index, val in enumerate(arr, 1):
        delta = val - index
        delta = abs(delta)
        ans = gcd(ans, delta)
    print(ans)
for _ in range(int(input())):
    solve() 
