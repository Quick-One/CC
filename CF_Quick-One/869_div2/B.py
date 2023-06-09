from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N = int(input())

    if N == 1:
        print(1)
    elif N % 2 == 1:
        print(-1)
    else:
        ans = list(range(1, N+1))
        for i in range(0, N, 2):
            ans[i], ans[i+1] = ans[i+1], ans[i]
        print(*ans) 
for _ in range(int(input())):
    solve()