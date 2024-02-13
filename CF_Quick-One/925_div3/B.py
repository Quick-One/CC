from sys import stdin
def input(): return stdin.readline()[:-1]

from string import ascii_lowercase

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    k = s//n
    
    buffer = 0
    for i in range(n):
        if a[i] >= k:
            buffer += a[i] - k
            continue
        if a[i] + buffer < k:
            print('No')
            return
        else:
            buffer -= k - a[i]
    print('Yes')
            
    
        
        

for _ in range(int(input())):
    solve()