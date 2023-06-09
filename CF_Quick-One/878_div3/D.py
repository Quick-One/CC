from sys import stdin
def input(): return stdin.readline()[:-1]

def func(arr, maxi):
    ensured = arr[0] + maxi
    ans = 1

    for i in arr[1:]:
        if i - maxi <= ensured:
            continue
        else:
            ans += 1
            ensured = i + maxi
    return ans <= 3

def solve():
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    
    if N <= 3:
        print(0)
        return
    
    lo = 0
    hi = 10**9
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if func(arr, mid):
            hi = mid
        else:
            lo = mid + 1
    print(lo)


for _ in range(int(input())):
    solve()