from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(0, N-1):
        if A[i] > A[i + 1]:
            ans = max(ans, max(A[i], A[i + 1]))
    print(ans)

for _ in range(int(input())):
    solve()