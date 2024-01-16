from bisect import bisect_left
from sys import stdin
def input(): return stdin.readline()[:-1]


def MOD(x, y):
    v = x % y
    if v:
        return v
    return y


def solve():
    N, Q = map(int, input().split())

    Arr = []
    Multiplier = []
    for _ in range(N):
        a, b = map(int, input().split())
        if a == 1:
            Arr.append(b)
            Multiplier.append(1)
        else:
            Multiplier[-1] *= (b+1)

    START = []
    END = []

    for i in range(len(Arr)):
        if len(START) == 0:
            START.append(1)
        else:
            START.append(END[-1] + 1)
        END.append(START[-1] * Multiplier[i])
        if START[-1] > 10**18 + 5:
            break

    ANS = []
    Query = list(map(int, input().split()))

    for index in Query:
        while True:
            pos = bisect_left(END, index)
            index = MOD(index, START[pos])
            pos2 = bisect_left(START, index)
            if START[pos2] == index:
                ANS.append(Arr[pos2])
                break

    print(*ANS)


for _ in range(int(input())):
    solve()
