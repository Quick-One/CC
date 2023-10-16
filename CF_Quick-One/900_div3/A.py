from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    if K in A:
        print("YES")
        return
    print("NO")

for _ in range(int(input())):
    solve() 