from sys import stdin
def input(): return stdin.readline()[:-1]

def oi():
    return int(input())
 
def ti():
    return map(int, input().split())
 
def mi():
    return list(map(int, input().split()))
 
def solve():
    x,y = ti()
    arr = []
    for i in range(y, x+1):
        arr.append(i)
    for i in range(x-1, y, -1):
        arr.append(i)
    print(len(arr))
    print(*arr) 
    
for _ in range(oi()):
    solve()