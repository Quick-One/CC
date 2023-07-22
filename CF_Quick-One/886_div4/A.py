from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    A = list(map(int, input().split()))
    A.sort()
    if (A[-1] + A[-2]) >= 10:
        print("YES")
    else:
        print("NO")

for _ in range(int(input())):
    solve() 