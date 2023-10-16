from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    n, k, x = map(int, input().split())

    # sum of number from 1, 2 , ..k 
    low = (k * (k + 1)) // 2


    # sum of numbers form n, n-1, .. n-k+1
    hi = (k * (2 * n - k + 1)) // 2

    if low <= x <= hi:
        print("YES")
    else:
        print("NO")



for _ in range(int(input())):
    solve() 