from sys import stdin
def input(): return stdin.readline()[:-1]

from string import ascii_lowercase
from collections import Counter

def f(x):
    first= x[0]
    cnt = 1
    for i in range(1,len(x)):
        if x[i] == first:
            cnt += 1
        else:
            break
    return cnt

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    start = f(a)
    end = f(a[::-1])
    val = float('inf')
    if a[0] == a[-1]:
        if start == end == n:
            print(0)
            return
        else:
            val = n - (start + end)
    y = min(n-start, n - end,val)
    print(y)
    
            
    
        
        

for _ in range(int(input())):
    solve()