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
    arr1 = mi()
    arr2 = mi()

    a = [0] * N
    b = [0] * N
    
    for i in range(N):
        a[i] = max (arr1[i], arr2[i])
        b[i] = min (arr1[i], arr2[i])

    # get the max elemenent in a
    max_a = max(a)
    max_b = max(b)

    if max_a == a[-1] and max_b == b[-1]:
        print("YES")
    else:
        print("NO")
    
for _ in range(oi()):
    solve()