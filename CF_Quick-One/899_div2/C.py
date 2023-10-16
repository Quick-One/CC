from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N = int(input())
    A = list(map(int, input().split()))

    if N == 1:
        print(max(0, A[0]))
    else:
        s = max(0, A[0], A[0]+A[1])
        for i in range(2, N):
            if A[i] > 0:
                s+=A[i]
        print(s)
        

    

for _ in range(int(input())):
    solve()