from sys import stdin
def input(): return stdin.readline()[:-1]


def check(x, A, K):
    s=0
    for i in A:
        if i < x:
            s += x - i
    if s <= K:
        return False
    else:
        return True

def solve():
    N, K = map(int, input().split())
    A  = list(map(int, input().split()))

    l, h = 1, 10**18

    ## last false binary search
    while l < h:
        mid = l + (h - l + 1) // 2

        if check(mid, A, K):
            h = mid - 1
        else:
            l = mid
    
    print(l)



for _ in range(int(input())):
    solve()