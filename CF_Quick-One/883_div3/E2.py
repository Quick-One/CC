from sys import stdin
def input(): return stdin.readline()[:-1]


d = {}
for i in range(3, 60):
    d[i] = int(pow(10 , 18/(i-1))) + 2 

def binary_search(n, N):
    lo = 2
    hi = d[n]
    while lo < hi:
        mid = lo + (hi - lo) // 2
        values = (pow(mid, n) - 1) // (mid - 1)
        if values >= N:
            hi = mid
        else:
            lo = mid + 1
    if (pow(lo, n) - 1) // (lo - 1) == N:
        return True
    else:
        return False

def solve():
    N = int(input())
    for n in range(3, 60):
        out = binary_search(n, N)
        if out:
            print("YES")
            return
    print("NO")



for _ in range(int(input())):
    solve()
