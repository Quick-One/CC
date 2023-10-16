from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N = int(input())
    a = list(map(int, input().split()))
    arr = []
    nex = 1
    for i in a:
        if i == nex:
            nex += 1
        arr.append(nex)
        nex += 1
    print(arr[-1])

for _ in range(int(input())):
    solve()