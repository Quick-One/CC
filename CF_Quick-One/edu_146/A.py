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
    if a % 2== 0:
        print("Yes")
        return
    if b % 2 == 0:
        print('No')
        return
    if a-b < 0:
        print('No')
        return
    print('Yes')
    
for _ in range(oi()):
    solve()