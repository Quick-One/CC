from sys import stdin
def input(): return stdin.readline()[:-1]


from collections import Counter
def solve():
    N, d, a = map(int, input().split())
    arr = list(map(int, input().split()))
    alpha = N * d + a
    arr = sorted(set(arr))
    ans = (N - len(arr)) * d
    N = len(arr)
    c = float('inf')
    for i, x in enumerate(arr, 1):
        cost = (N-i)*d
        cost += (x-i) * a
        c = min(c, cost)
    print(min(ans + c, alpha))

for _ in range(int(input())):
    solve()
