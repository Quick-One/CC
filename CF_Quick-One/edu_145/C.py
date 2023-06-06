from sys import stdin
def input(): return stdin.readline()[:-1]

def oi():
    return int(input())
 
def ti():
    return map(int, input().split())
 
def mi():
    return list(map(int, input().split()))
 
def bin_search(lo, hi, K):
    while lo < hi:
        mid = lo + (hi - lo + 1)//2
        p = mid
        s = (p * (p + 1)) // 2
        d = K - s
        b = d >= 0
        if not b:
            hi = mid - 1
        else:
            lo = mid
    return lo

def solve():
    N, K = ti()
    if K == 0:
        for _ in range(N):
            print(-1000, end=' ')
        print()
        return
    
    p = bin_search(1, 100, K)


    s = (p * (p + 1)) // 2
    d = K - s

    if d == 0:
        for _ in range(N - p):
            print(-1000, end=' ')
        for _ in range(p):
            print(2, end=' ')
        print()
        return
    
    neg_val = - (2 * (p - d) + 1)
    filler_freq = N - p - 1


    for _ in range(filler_freq):
        print(-1000, end=' ')
    print(neg_val, end=' ')
    for _ in range(p):
        print(2, end=' ')
    print()

for _ in range(oi()):
    solve()