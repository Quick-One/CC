from sys import stdin
def input(): return stdin.readline()[:-1]

from math import comb

def solve():
    N = int(input())
    ARR = list(map(int, input().split()))
    ARR.sort()
    var = ARR[0]
    count = 1
    COUNTS = [] # list of tupples
    for i in range(1, N):
        if ARR[i] == var:
            count += 1
        else:
            COUNTS.append((var, count))
            var = ARR[i]
            count = 1
    COUNTS.append((var, count))
    
    if N < 3:
        print(0)
        return
    
    ANS = 0
    cum = 0
    for a, b in COUNTS:
        # equilateral

        if b >= 3:
            ANS += comb(b, 3)
        # isosceles
        if b >= 2:
            ANS += comb(b, 2) * cum
        cum += b
    
    print(ANS)
            
    # print(COUNTS)

for _ in range(int(input())):
    solve()