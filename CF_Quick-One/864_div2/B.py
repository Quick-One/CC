from sys import stdin
def input(): return stdin.readline()[:-1]

def oi():
    return int(input())
 
def ti():
    return map(int, input().split())
 
def mi():
    return list(map(int, input().split()))
 

def rot180(m):
    # rotates a matrix 180 degrees
    return [row[::-1] for row in m[::-1]]

def solve():
    N,K = ti()
    a = []
    for i in range(N):
        a.append(mi())



    b = rot180(a)
    b = [row.copy() for row in b]
    # Take XOR of each element of a and b
    ans = 0
    for i in range(N):
        for j in range(N):
            ans += a[i][j] ^ b[i][j]
    ans //=2 
    if ans > K:
        print("NO")
        return
    if ans == K:
        print("YES")
    else:
        if N%2 == 1:
            print("YES")
            return
        
        delta = K - ans
        if delta % 2 == 0:
            print("YES")
        else:
            print("NO")
    
for _ in range(oi()):
    solve()