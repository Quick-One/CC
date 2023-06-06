from sys import stdin
def input(): return stdin.readline()[:-1]
 
from collections import Counter
def solve():
    N = int(input())
    s = input().strip()
 
    c = Counter(s)
    a = c['(']
    b = c[')']
 
    if a != b:
        print(-1)
        return
    d = []
    curr = 0
    abc = [0]
 
    for i in s:
        if i == '(':
            curr += 1   
        else:
            curr -= 1
        abc.append(curr)
    positive = False
    negative = False
    for i in abc:
        if i < 0:
            negative = True
        if i > 0:
            positive = True
    if positive and negative:
        print(2)
        answer = [1] * N
        for i in range(1,N+1):
            if abc[i] < 0:
                answer[i-1] = 2
            if abc[i] == 0 and abc[i-1] < 0:
                answer[i-1] = 2
        print(*answer)  
    else:
        print(1)
        ans = [1] * N
        print(*ans)
 
        
 
for _ in range(int(input())):
    solve()