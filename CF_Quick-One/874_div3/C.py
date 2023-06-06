from sys import stdin
def input(): return stdin.readline()[:-1]


def even(arr, odds, evens):
    for i in arr:
        if i % 2 == 0:
            continue
        else:
            if len(odds) == 0:
                return -1
            else:
                if i - odds[0] <= 0:
                    return -1
                else:
                    continue
    return 1

def odd(arr, odds, evens):
    for i in arr:
        if i % 2 == 1:
            continue
        else:
            if len(odds) == 0:
                return -1
            else:
                if i - odds[0] <= 0:
                    return -1
                else:
                    continue
    return 1
def solve():
    N = int(input())
    arr = list(map(int, input().split()))

    evens = []
    odds = []
    for i in arr:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    evens.sort()
    odds.sort()

    ans = max(odd(arr, odds, evens), even(arr, odds, evens))
    # print(odd(arr, odds, evens), even(arr, odds, evens))
    if ans == 1:
        print("YES")
    else:
        print("NO")


for _ in range(int(input())):
    solve()