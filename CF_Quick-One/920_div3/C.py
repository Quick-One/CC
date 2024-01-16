from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N,f, a, b = map(int, input().split())
    Arr = list(map(int, input().split()))
    Arr.insert(0,0)
    
    for i in range(0, N + 1):
        if f <= 0:
            print("NO")
            return
        if i == N:
            print("YES")
            return
        nothing = Arr[i + 1] - Arr[i]
        nothing *= a
        nothing = min(nothing,  b )
        f -= nothing
        
    
    
for _ in range(int(input())):
    solve()