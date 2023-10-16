from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N = int(input())
    Arr = list(map(int, input().split()))

    if (N%2) == 0:
        print(2)
        print(1, N)
        print(1, N)
    else:
        print(4)
        print(1, N)
        print(1, N-1)
        print(N-1, N)
        print(N-1, N)

for _ in range(int(input())):
    solve()