def oi():
    return int(input())
 
def ti():
    return map(int, input().split())
 
def mi():
    return list(map(int, input().split()))
 
from queue import PriorityQueue


def solve():
    n = oi()
    arr = mi()
    ans = 0
    temp = PriorityQueue()
    for i in arr:
        if i == 0 and not temp.empty():
            ans -= temp.get()
        else:
            temp.put(-i)
    print(ans)
        
    
for _ in range(oi()):
    solve()