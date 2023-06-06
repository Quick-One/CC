from sys import stdin
from sys import stdout

def oi():
    return int(input())
 
def ti():
    return map(int, input().split())
 
def mi():
    return list(map(int, input().split()))
 
def solve():
    
    N = oi()
    arr = mi()
    ans = 0
    digit = 0

    while True:
        q = []
        s = 0
        for i in range(1, N+1):
            if i & (1 << digit):
                q.append(i)
                s += arr[i-1]
        
        if len(q) == 0:
            break
        print('?', len(q), *q)
        stdout.flush()
        s1 = int(input())
        if s1 != s:
            ans += (1 << digit)
        digit += 1
    print(f'! {ans}')
    stdout.flush()
            
    
for _ in range(oi()):
    solve()