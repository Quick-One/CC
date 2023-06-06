from sys import stdin
def input(): return stdin.readline()[:-1]

def Counter(arr):
    d = {}
    for i in arr:
        if i not in d:
            d[i] = 0
        d[i] += 1
    return d

def MEX(count):
    i = 0
    while True:
        if i not in count:
            return i
        i += 1
 
def solve():
    N = int(input())
    arr = list(map(int, input().split()))
    c = Counter(arr)
    x = MEX(c)
    new_MEX = x + 1
    if new_MEX in c:
        indices = []
        for i, val in enumerate(arr):
            if val  == new_MEX:
                indices.append(i)
        l,r = min(indices), max(indices)
        for i in range(l, r +1):
            arr[i] = x
        c2 = Counter(arr)
        if MEX(c2) == new_MEX:
            print("YES")
        else:
            print("NO")
    else:
        for i, v in c.items():
            if (i<x and v > 1) or (i>x):
                print("YES")
                return
        print("NO")
 
 
t = int(input())
for _ in range(t):
    solve()
