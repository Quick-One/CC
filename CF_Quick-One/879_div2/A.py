from sys import stdin
def input(): return stdin.readline()[:-1]


def solve():
    N = int(input())
    A = list(map(int, input().split()))

    s = sum(A)
    cnt = A.count(-1)
    op = 0
    while s < 0 or cnt % 2 == 1:
        op += 1
        s += 2
        cnt -= 1
    print(op)
    
        
        


for _ in range(int(input())):
    solve()