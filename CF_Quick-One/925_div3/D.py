from sys import stdin
def input(): return stdin.readline()[:-1]
from collections import defaultdict

def solve():
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    
    d = defaultdict(int)
    ans = 0
    for i in range(n):
        identity = (a[i] % x, a[i] % y)
        need = ((x - a[i]) %x , a[i] % y)
        ans += d[need]
        d[identity] += 1
    
    print(ans)
    
for _ in range(int(input())):
    solve()