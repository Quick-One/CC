from sys import stdin
def input(): return stdin.readline()[:-1]

from math import isqrt
from collections import deque

def solve():
    N = int(input())
    s = input().strip()

    temp  =[]
    for i in s:
        if i in ['a', 'e']:
            temp.append(0)
        else:
            temp.append(1)
    temp = deque(temp)
    
    ANS = []
    
    while True:
        if len(temp) == 2:
            ANS.append(2)
            break
        elif len(temp) == 3:
            ANS.append(3)
            break
        
        c = temp[3]
        if c == 0:
            ANS.append(2)
            temp.popleft()
            temp.popleft()
        else:
            ANS.append(3)
            temp.popleft()
            temp.popleft()
            temp.popleft()
    
    final = []
    s = list(s[::-1])
    for i in ANS:
        for _ in range(i):
            final.append(s.pop())
        final.append('.')
    print(''.join(final[:-1]))

for _ in range(int(input())):
    solve()