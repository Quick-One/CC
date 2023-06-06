from sys import stdin
def input(): return stdin.readline()[:-1]

def oi():
    return int(input())
 
def ti():
    return map(int, input().split())
 
def mi():
    return list(map(int, input().split()))
 
def solve():
    n, m = ti()
    x1, y1, x2, y2 = ti()

    ans = 4
    # check if x1, y1 is a corner point
    if x1 == 1 and y1 == 1:
        ans = min(ans, 2)
    elif x1 == 1 and y1 == m:
        ans = min(ans, 2)
    elif x1 == n and y1 == 1:
        ans = min(ans, 2)
    elif x1 == n and y1 == m:
        ans = min(ans, 2)
    # check if x1, y1 is on the edge
    elif x1 == 1 or x1 == n:
        ans = min(ans, 3)
    elif y1 == 1 or y1 == m:
        ans = min(ans, 3)
    # check if x1, y1 is in the middle
    else:
        ans = min(ans, 4)
    

    # check if x2, y2 is a corner point
    if x2 == 1 and y2 == 1:
        ans = min(ans, 2)
    elif x2 == 1 and y2 == m:
        ans = min(ans, 2)
    elif x2 == n and y2 == 1:
        ans = min(ans, 2)
    elif x2 == n and y2 == m:
        ans = min(ans, 2)
    # check if x2, y2 is on the edge
    elif x2 == 1 or x2 == n:
        ans = min(ans, 3)
    elif y2 == 1 or y2 == m:
        ans = min(ans, 3)
    # check if x2, y2 is in the middle
    else:
        ans = min(ans, 4)
    print(ans)


for _ in range(oi()):
    solve()