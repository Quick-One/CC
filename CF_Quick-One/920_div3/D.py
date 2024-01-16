from sys import stdin
def input(): return stdin.readline()[:-1]
from collections import deque
def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    A = deque(A)    
    
    B = list(map(int, input().split()))
    B.sort()
    B = deque(B)
    
    ans = 0
    while len(A):
        d1 = abs(A[0] - B[0])
        d2 = abs(A[-1] - B[-1])
        
        if d1 > d2:
            ans += d1
            A.popleft()
            B.popleft()
        
        else:
            ans += d2
            A.pop()
            B.pop()
            
    print(ans)

for _ in range(int(input())):
    solve()
    