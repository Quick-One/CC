from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N = int(input())
    arr = list(map(int, input().split()))

    i1 = arr.index(1)
    i2 = arr.index(2)
    iN = arr.index(N)

    if i2 < iN < i1 or i1 < iN < i2:
        print(i1+1, i1+1)
    elif i1 < i2 < iN or iN < i2 < i1:
        print(i2+1, iN+1)
    else:
        print(iN+1, i1+1)

for _ in range(int(input())):
    solve()