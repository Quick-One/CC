from sys import stdin
def input(): return stdin.readline()[:-1]

d = {}


for a in range(32):
    for b in range(32):
        diff = 2 ** (a) - 2 ** (b)
        if diff == 0:
            continue
        d[diff] = (a,b)

def solve():
    N = int(input())
    A = list(map(int, input().split()))

    s = sum(A)
    if (s % N != 0):
        print("No")
        return
    avg = s // N
    
    
    out = []
    ine = []

    for i in A:
        flow  = i - avg
        if flow == 0:
            continue
        if flow not in d:
            print("No")
            return
        a,b = d[flow]
        out.append(a)
        ine.append(b)
    out.sort()
    ine.sort()
    if (out == ine):
        print("Yes")
    else:
        print("No")
    
        



for _ in range(int(input())):
    solve()