def oi():
    return int(input())
 
def ti():
    return map(int, input().split())
 
def mi():
    return list(map(int, input().split()))


MOD = 998244353

from math import log2

def solve_for_k(l, r):
    n = 0
    while l*2 <= r:
        l *= 2
        n += 1
    return n

def solve():
    l, r = ti()
    FIRST = solve_for_k(l, r)
    SECOND = 0

    if FIRST == 0:
        SECOND = r - l + 1
        SECOND %= MOD
        print(FIRST+1, SECOND)
        return
    
    multiplier = 2**FIRST
    upper_end_2 = r//multiplier
    SECOND += upper_end_2 - l + 1
    SECOND %= MOD

    multiplier //= 2
    multiplier *= 3

    if l * multiplier <= r:
        upper_end_3 = r//multiplier
        SECOND += (upper_end_3 - l + 1) * (FIRST)
        SECOND %= MOD

    print(FIRST+1, SECOND)
    

    
for _ in range(oi()):
    solve()
