from sys import stdin
def input(): return stdin.readline()[:-1]


def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ANS = A[N-1] - A[0] + A[-1] - A[N]
    print(ANS)
    for i in range(N):
        print(A[i], A[i+N])
for _ in range(int(input())):
    solve()