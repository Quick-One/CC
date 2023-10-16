from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    n, MEX, x  = map(int, input().split())
    
    if 0 <= (x + 1) <= MEX - 1 :
        print(-1) 
        return
    if n < MEX:
        print(-1)
        return
    


    s = (MEX - 1) * (MEX) // 2
    if x == MEX:
        x -= 1

    s += (n - MEX) * x
    print(s) 

for _ in range(int(input())):
    solve()