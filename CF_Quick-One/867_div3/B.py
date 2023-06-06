from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    
    if N == 2:
        print(arr[0] * arr[1])
    else:
        a = arr[-1] * arr[-2]
        b = arr[0] * arr[1]
        print(max(a, b))
    

for _ in range(int(input())):
    solve()