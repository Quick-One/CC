from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N = int(input())
    A = []
    for i in range(N):
        a,b=  map(int, input().split())
        if a <= 10:
            A.append((b, i+1))
    print(max(A)[1])

for _ in range(int(input())):
    solve() 