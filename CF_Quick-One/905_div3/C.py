from sys import stdin
def input(): return stdin.readline()[:-1]

from collections import Counter

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    if K != 4:
        a = [i % K for i in A]
        if 0 in a:
            print(0)
        else:
            print(K - max(a))
    else:
        a = [i % K for i in A]
        if 0 in a:
            print(0)
            return
        ans_temp = K - max(a)
        b = [i%2 for i in a]
        b.sort()
        if len(b) >= 2:
            ans_temp = min(ans_temp, b[0] + b[1])
        print(ans_temp) 


for _ in range(int(input())):
    solve()