from sys import stdin
def input(): return stdin.readline()[:-1]

from collections import deque

def solve():
    N, k = map(int, input().split())
    d = deque(sorted((map(int, input().split()))))
    prefix_sum = [0] * (N + 1)
    for i in range(N):
        prefix_sum[i + 1] = prefix_sum[i] + d[i]
    r = N
    l = 2*k
    # print(d)
    # print(prefix_sum)
    ans = -float('inf')
    for _ in range(k+1):
        # print(l,r)
        # print(prefix_sum[r], prefix_sum[l])
        # print(prefix_sum[r] - prefix_sum[l])
        ans = max(ans, prefix_sum[r] - prefix_sum[l])
        r -= 1
        l -= 2
    print(ans)

for _ in range(int(input())):
    solve()