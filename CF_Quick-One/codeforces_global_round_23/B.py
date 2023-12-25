from sys import stdin
def input(): return stdin.readline()[:-1]

from collections import deque

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    
    index0 = deque()
    index1 = deque()
    
    for i, e in enumerate(A):
        if e == 0:
            index0.append(i)
        else:
            index1.append(i)
    
    ans = 0
    while True:
        if len(index0) != 0 and len(index1) != 0:
            if index1[0] < index0[-1]:
                ans += 1
                index1.popleft()
                index0.pop()
            
            elif index1[-1] < index0[-1]:
                ans += 1
                index0.pop()
                
            else:
                break     
        else:
            break

    print(ans)      

for _ in range(int(input())):
    solve()