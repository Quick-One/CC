from sys import stdin
def input(): return stdin.readline()[:-1]

from collections import deque

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    ANS = [0] * N 
    ANS[0] = A[-1]
    for i in range(1, N):
        ANS[i] = A[i-1]

    d = {}
    for i, j in enumerate(ANS):
        d[j] = i
    
    ANS2 = []
    for i in range(N):
        ANS2.append(d[i+1]+1)
    print(*ANS2)

for _ in range(int(input())):
    solve()