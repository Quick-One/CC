from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    if 1 in A:
        print("YES")
    else:
        print("NO")

for _ in range(int(input())):
    solve()