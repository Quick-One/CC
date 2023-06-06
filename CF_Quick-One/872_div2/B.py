from sys import stdin
def input(): return stdin.readline()[:-1]


def solve():
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    MAX = arr[-1]
    MAX2 = arr[-2]
    first_min = arr[0]
    second_min = arr[1]
    a,b = min(N, M), max(N, M)
    other = (N-1) * (M-1)

    ans = MAX + other*first_min + (a-1)*second_min + (b-1) * first_min
    ans *= -1
    ans += MAX * (N * M)
    # print(ans)

    ans2 = first_min + MAX2*(a-1) + MAX*(b-1) + MAX*(other)
    ans2 -= first_min * (N*M)
    print(max(ans, ans2))

for _ in range(int(input())):
    solve()