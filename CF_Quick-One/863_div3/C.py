from sys import stdin
def input(): return stdin.readline()[:-1]

def oi():
    return int(input())
 
def ti():
    return map(int, input().split())
 
def mi():
    return list(map(int, input().split()))
 
def solve():
    n = oi()
    arr = mi()
    ans = [0] * n

    if n == 2:
        print(arr[0], arr[0])
        return

    for i in range(n-2):
        a,b = arr[i], arr[i+1]
        if b >  a:
            ans[i+1] = a
            ans[i+2] = b
        elif b < a:
            ans[i+1] = b
            ans[i] = a
        else:
            ans[i+1] = b
    print(*ans)

            
for _ in range(oi()):
    solve()