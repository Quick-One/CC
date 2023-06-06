from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N = int(input())
    if N == 1:
        print(1)
    elif N % 2 == 1:
        print(-1)
    else:
        ans = []
        ans.append(N)
        p = 0
        n = N//2
        for i in range(N-1, n, -1):
            a = i
            delta = (a - p) % N
            p += delta
            p %= N
            ans.append(delta)
            a = N - a
            delta = (a - p) % N
            p += delta
            p %= N
            ans.append(delta)
        ans.append(1)
        print(*ans)
for _ in range(int(input())):
    solve()