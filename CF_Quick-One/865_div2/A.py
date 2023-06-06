from sys import stdin
def input(): return stdin.readline()[:-1]

def oi():
    return int(input())
 
def ti():
    return map(int, input().split())
 
def mi():
    return list(map(int, input().split()))
 
def solve():
    a,b = ti()
    if 1 in (a,b):
        print(1)
        print(a,b)
    else:
        print(2)
        print(a-1, 1)
        print(a,b)
    
for _ in range(oi()):
    solve()