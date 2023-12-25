from sys import stdin
def input(): return stdin.readline()[:-1]

from collections import Counter

def solve():
    N = int(input())
    string = input().strip()
    c = Counter(string)

    v = list(c.values())
    v.sort()
    
    ANS = v[-1] -  sum(v[:-1])
    if ANS > 0:
        print(ANS)
    else:
        print(ANS & 1)

for _ in range(int(input())):
    solve()