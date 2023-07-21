from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N = int(input())
    ans = 0
    for _ in range(N):
        a, b = map(int, input().split())
        ans += (a > b)
    print(ans)


for _ in range(int(input())):
    solve()
