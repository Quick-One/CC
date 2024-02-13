from sys import stdin
def input(): return stdin.readline()[:-1]
 
def solve():
    N = int(input())
    a, b, c =input().strip(), input().strip(), input().strip()
    
    for i in range(N):
        c1, c2, c3 = a[i], b[i], c[i]
        if c1 != c2 and c2 != c3 and c3 != c1:
            print('YES')
            return
        elif (c1 == c2 and c2 != c3):
            print('YES')
            return
        
    print('NO')
 
for _ in range(int(input())):
    solve()