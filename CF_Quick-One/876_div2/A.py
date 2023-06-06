from sys import stdin
def input(): return stdin.readline()[:-1]

def ceildiv(a, b):
    return -(a // -b)

def solve():
    N, K = map(int, input().split())
    print(ceildiv(N-1, K) + 1)
    

for _ in range(int(input())):
    solve()