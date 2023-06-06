from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ans = []
    for i in A:
        ans.append(N - i + 1)
    print(*ans)

for _ in range(int(input())):
    solve()