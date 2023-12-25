from sys import stdin
def input(): return stdin.readline()[:-1]

from collections import Counter

def solve():
    N, K = map(int, input().split())
    S = input()
    c = Counter(S)

    odd = 0
    even = 0
    for v in c.values():
        if v % 2 == 0:
            even += 1
        else:
            odd += 1

    if (N - K) % 2 == 0:
        if odd <= K:
            print('YES')
        else:
            print("NO")
    else:
        if odd -1 <= K:
            print('YES')
        else:
            print("NO")


for _ in range(int(input())):
    solve()