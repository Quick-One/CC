from sys import stdin
def input(): return stdin.readline()[:-1]

def oi():
    return int(input())
 
def ti():
    return map(int, input().split())
 
def mi():
    return list(map(int, input().split()))
 
def solve():
    N = int(input())
    arr = mi()
    l = 0
    r = N-1
    mini = 1
    maxi = N

    while l <= r:
        if arr[l] == mini:
            l += 1
            mini += 1
        elif arr[l] == maxi:
            l += 1
            maxi -= 1
        elif arr[r] == mini:
            r -= 1
            mini += 1
        elif arr[r] == maxi:
            r -= 1
            maxi -= 1
        else:
            break

    if l < r:
        print(l+1, r+1)
    else:
        print(-1)    
    
for _ in range(oi()):
    solve()