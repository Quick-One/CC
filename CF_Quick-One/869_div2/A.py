from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N, K = map(int, input().split())
    initial = input().strip()
    ans = 1
    for _ in range(N-1):
        i2 = input().strip()
        if i2 == initial:
            ans += 1
    print(ans)

for _ in range(int(input())):
    solve()