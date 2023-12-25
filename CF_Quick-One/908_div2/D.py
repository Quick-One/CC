from sys import stdin
def input(): return stdin.readline()[:-1]

from collections import deque

def solve():
    _ = input()
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    B = deque(sorted(B))
    A.reverse()
    A = deque(A)
    
    ANS = []

    while len(A) != 0 and len(B) != 0:
        
        if A[0] <= B[0]:
            ANS.append(A.popleft())
        else:
            ANS.append(B.popleft())
    ANS += A + B
    
    ANS.reverse()
    print(*ANS)


for _ in range(int(input())):
    solve()