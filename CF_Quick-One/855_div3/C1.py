def oi():
    return int(input())
 
def ti():
    return map(int, input().split())
 
def mi():
    return list(map(int, input().split()))
 
from bisect import insort
def solve():
    n = oi()
    arr = mi()
    ans = 0
    temp = []
    for i in arr:
        if i == 0 and len(temp) > 0:
            ans += temp.pop()
        else:
            insort(temp, i)
    print(ans)
        
    
for _ in range(oi()):
    solve()