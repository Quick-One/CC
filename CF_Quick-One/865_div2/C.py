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
    for i in range(1, N-1):
        delta = arr[i] - arr[i-1]
        arr[i] -= delta
        arr[i+1] -= delta

    a,b = arr[0], arr[-1]
    if a <= b:
        print("YES")
    else:
        if N % 2 == 0:
            print("NO")
        else:
            print("YES")

for _ in range(oi()):
    solve()