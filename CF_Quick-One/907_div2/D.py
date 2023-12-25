from sys import stdin
def input(): return stdin.readline()[:-1]

def log(x, base):
    # floor log using binary search
    l, r = 0, 100
    while r - l > 1:
        m = (l + r) // 2
        if base ** m <= x:
            l = m
        else:
            r = m
    return l



d  = []
def precompute():
    for f in range(2, 60):
        l, r = 2 ** f, 2 ** (f + 1) - 1
        l1, l2 = log(l, f), log(r, f)
        for n in range(l1, l2 + 1):
            lo, hi = max(l, f ** n), min(r, f ** (n + 1) - 1)
            d.append((n, lo, hi))

precompute()

def find_intersection(l1, r1, l2, r2):
    if l1 > r2 or l2 > r1:
        return 0
    return min(r1, r2) - max(l1, l2) + 1
    


MOD = 10 ** 9 + 7


def solve():
    l, r = map(int, input().split())
    ANS = 0
    for n, lo, hi in d:
        ANS += find_intersection(l, r, lo, hi) * n
        ANS %= MOD
    print(ANS)
    
for _ in range(int(input())):
    solve()