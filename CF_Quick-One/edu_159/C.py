from sys import stdin
def input(): return stdin.readline()[:-1]

from math import gcd

def solve():
    N = int(input())    
    Arr = list(map(int, input().split()))

    if N == 1:
        print(1)
        return

    mini = min(Arr)
    Arr = [x - mini for x in Arr]
    Arr.sort()
    diff = []
    for i in range(N-1):
        diff.append(Arr[i+1] - Arr[i])
    gc = diff[0]
    for i in range(1, len(diff)):
        gc = gcd(gc, diff[i])
    Arr = [x // gc for x in Arr]
    # print(Arr)

    if Arr[-1] == len(Arr) - 1:
        need = len(Arr)
    else:
        c = set(Arr)
        maxi = max(Arr)
        while maxi in c:
            maxi -= 1
        need = maxi


    Arr.append(need)
    maxi = max(Arr)
    ANS=0
    for i in Arr:
        ANS += maxi - i
    print(ANS)
    
    

for _ in range(int(input())):
    solve()