from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    n, k = map(int, input().split())

    if k > 32:
        print(n + 1)
    else:
        print(min(n+1, 2**k))

for _ in range(int(input())):
    solve()