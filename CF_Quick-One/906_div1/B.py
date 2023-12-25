from sys import stdin
def input(): return stdin.readline()[:-1]

from fractions import Fraction

def solve():
    N, C = map(int, input().split())
    A = list(map(int, input().split()))

    rsize = [(Fraction(A[i-1], C), i) for i in range(1, N+1)]
    size = rsize[0][0]

    rsize = rsize[1:]
    rsize.sort(key = lambda x: x[1] - x[0])
    flag = True
    for i in range(N-1):
        if size + rsize[i][0] >= rsize[i][1]:
            size += rsize[i][0]
        else:
            flag = False
            break
    

    if flag:
        print("YES")
    else:
        print("NO")
        





for _ in range(int(input())):
    solve()