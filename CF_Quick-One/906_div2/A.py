from sys import stdin
def input(): return stdin.readline()[:-1]

from collections import Counter

def solve():
    N = int(input())
    A = list(map(int, input().split()))

    c = Counter(A)
    if len(c) == 1:
        print("Yes")
    elif len(c) == 2:
        vals = list(c.values())
        vals.sort()

        if N % 2 == 0:
            k = N// 2
            if vals[0] == k and vals[1] == k:
                print("Yes")
            else:
                print("No")
        else:
            k = N // 2
            if vals[0] == k and vals[1] == k + 1:
                print("Yes")
            else:
                print("No")
    else:
        print("No")


for _ in range(int(input())):
    solve()