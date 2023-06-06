from sys import stdin
def input(): return stdin.readline()[:-1]

def oi():
    return int(input())
 
def ti():
    return map(int, input().split())
 
def mi():
    return list(map(int, input().split()))


def f(arr, N):
    s = 0
    arr = sorted(arr)
    for i in range(1, N):
        d = arr[i] - arr[i-1]
        s += i * (N-i) * d
    return s

def solve():
    N, M = ti()
    arr = []
    for _ in range(N):
        arr.append(mi())

    ans = 0
    for col in zip(*arr):
        ans += f(col, N)
    print(ans)
    
    
for _ in range(oi()):
    solve()