from sys import stdin, stdout
def input(): return stdin.readline()[:-1]

MOD = 10**9 + 7

def inverse(a):
    return pow(a, -1, MOD)
    
from random import getrandbits
RANDOM = getrandbits(32)

class Wrapper(int):
    def __init__(self, x):
        int.__init__(x)
    def __hash__(self):
        return super(Wrapper, self).__hash__() ^ RANDOM

from collections import Counter
ANSWERS = []
def solve():
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    c = Counter(map(Wrapper, arr))

    # c = Counter(arr) # ???? Bottle neck O(N^2)
    # arr = sorted(set(arr))
    ########################
    # NOT USING SETS TO PREVENT O(N^2) execution
    arr = sorted(arr)
    arr = [Wrapper(i) for i in arr]
    a = []
    for i in arr:
        if len(a) == 0 or a[-1] != i:
            a.append(i)
    arr = a
    ########################

    K = len(arr)
    if K < M:
        ANSWERS.append(0)
        return
    l, r = 0, M - 1
    multiplier = 1
    for i in range(l, r + 1):
        multiplier *= c[arr[i]]
        multiplier %= MOD
    ans = 0
    while True:
        if arr[r] - arr[l] < M:
            ans += multiplier
            ans %= MOD
        if r == K - 1:
            break
        multiplier *= inverse(c[arr[l]])
        multiplier %= MOD
        l += 1
        r += 1
        multiplier *= c[arr[r]]
        multiplier %= MOD
    
    ANSWERS.append(ans)

for _ in range(int(input())):
    solve()

print('\n'.join(map(str, ANSWERS)))

