from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N = int(input())
    arr = [2*i for i in range(1, N+1)]
    print(*arr)

for _ in range(int(input())):
    solve() 
