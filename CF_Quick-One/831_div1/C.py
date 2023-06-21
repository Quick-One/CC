from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    ans = -1
    for i in range(2, N):
        ans = max(ans, 2*arr[i] - arr[i-1] - arr[0])
    for i in range(0, N-2):
        ans = max(ans, arr[-1] + arr[i+1] - 2*arr[i])
    print(ans)

for _ in range(int(input())):
    solve()