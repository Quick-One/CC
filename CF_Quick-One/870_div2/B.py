from sys import stdin
def input(): return stdin.readline()[:-1]
from math import gcd
def solve():
    N = int(input())
    arr = list(map(int, input().split()))
    a = set()

    for i in range(N):
        diff = abs(arr[i] - arr[-i-1])
        if diff == 0:
            continue
        a.add(diff)
    
    if len(a) == 0:
        print(0)
    else:
        print(gcd(*a))

    

for _ in range(int(input())):
    solve() 