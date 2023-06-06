from sys import stdin
def input(): return stdin.readline()[:-1]
 
def solve():
    X, K = map(int, input().split())
    if X% K != 0:
        print(1)
        print(X)
    else:
        print(2)
        a, b = K+1, X - K -1
        print(a, b)
 
for _ in range(int(input())):
    solve()