from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N = int(input())
    Arr = list(map(int, input().split()))
    prefix = [0] * (N + 1)
    for i in range(N):
        prefix[i + 1] = prefix[i] + Arr[i]

    ans = 0

    for div in range(1, N+1):
        if N % div != 0:
            continue
        a = []
        for i in range(N // div):
            a.append(prefix[(i + 1) * div] - prefix[i * div])
        ans = max(ans, max(a) - min(a))
    print(ans)

for _ in range(int(input())):
    solve()