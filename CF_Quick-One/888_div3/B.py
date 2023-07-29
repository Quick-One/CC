from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N = int(input())
    A = list(map(int, input().split()))

    B = sorted(A)

    for i, j in zip(A,B):
        if i%2 != j%2:
            print("NO")
            return
    print("YES")


for _ in range(int(input())):
    solve()