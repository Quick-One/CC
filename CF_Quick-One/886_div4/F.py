from sys import stdin
def input(): return stdin.readline()[:-1]
 
from collections import Counter

from random import getrandbits
 
RANDOM = getrandbits(32)
 
class Wrapper(int):
    def __init__(self, x):
        int.__init__(x)
    def __hash__(self):
        return super(Wrapper, self).__hash__() ^ RANDOM 

def solve():
    N = int(input())
    A = list(map(Wrapper, input().split()))
    ANS = [0] * (N+1)
    c = Counter(A)
    ones = c[1]
    del c[1]
    for i, v in c.items():
        for j in range(i, N+1, i):
            ANS[j] += v
    print(max(ANS) + ones)
 
 
    
 
for _ in range(int(input())):
    solve()