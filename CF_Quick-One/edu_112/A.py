from sys import stdin
def input(): return stdin.readline()[:-1]

def ceildiv(a, b):
    return -(a // -b)

def solve():
    N = int(input())
    ans = ceildiv(N * 5, 2)
    ans = ceildiv(ans, 5)
    if ans <= 3:
        print(15)
    else:
        print(ans * 5)


for _ in range(int(input())):
    solve()