from sys import stdin
def input(): return stdin.readline()[:-1]

def oi():
    return int(input())
 
def ti():
    return map(int, input().split())
 
def mi():
    return list(map(int, input().split()))
 
def solve():
    a,b,c = ti()
    if a + b == c:
        print("+")
    else:
        print("-")
    
for _ in range(oi()):
    solve()