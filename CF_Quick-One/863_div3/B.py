from sys import stdin
def input(): return stdin.readline()[:-1]

def oi():
    return int(input())
 
def ti():
    return map(int, input().split())
 
def mi():
    return list(map(int, input().split()))
 
def solve():
    n, x1, y1, x2, y2 = ti()
    a = max(abs(x1- n//2 - 0.5), abs(y1- n//2 - 0.5))
    b = max(abs(x2- n//2 - 0.5), abs(y2- n//2 - 0.5))

    ans = round(a -b)
    print(abs(ans))


    
for _ in range(oi()):
    solve()