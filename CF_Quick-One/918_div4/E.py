from sys import stdin
def input(): return stdin.readline()[:-1]

from math import isqrt
from collections import Counter
def solve():
    N = int(input())
    A = list(map(int, input().split()))
    
    b = []
    for index, e in enumerate(A):
        if index&1:
            b.append(-e)
        else:
            b.append(e)
    
    prefix = [0] * (N+1)
    for index, e in enumerate(b):
        prefix[index+1] = prefix[index] + e
    
    c = Counter(prefix)
    for i in c.values():
        if i > 1:
            print('YES')
            return
    print('NO')
        

    

for _ in range(int(input())):
    solve()