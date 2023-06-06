from sys import stdin
def input(): return stdin.readline()[:-1]

def oi():
    return int(input())
 
def ti():
    return map(int, input().split())
 
def mi():
    return list(map(int, input().split()))
 
def solve():
    N = oi()
    arr = mi()
    XOR = 0
    for i in arr:
        XOR ^= i
    if (N) %2 == 0:
        if XOR == 0:
            print(0)
        else:
            print(-1)
    else:
        print(XOR ^ 0)
    
for _ in range(oi()):
    solve()