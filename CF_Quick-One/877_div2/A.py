from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N = int(input())
    arr = list(map(int, input().split()))

    neg = False
    val = None
    for i in arr:
        if i < 0:
            neg = True
            val = i

    if neg:
        print(val)

    else:
        print(max(arr))

for _ in range(int(input())):
    solve()
