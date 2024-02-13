from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    # N = int(input())
    a, b, x =  map(int, input().split())
    if a == b:
        print(0)
        return
    
    if b > a:
        a, b = b, a 
    # print(a, b)
    # print(bin(a), bin(b))
    flag = False
    
    for dig in range(60, -1, -1):
        m = 1 << dig
        da, db = a & m, b & m
        if da == db:
            continue
        else:
            if da < db:
                continue
            
            
            if not flag:
                flag = True
                continue
            else:
                
                
                
                if m <= x:
                    x -= m
                    a ^= m
                    b ^= m
    print(abs(a - b))
    
    
    
    
for _ in range(int(input())):
    solve()