from sys import stdin
def input(): return stdin.readline()[:-1]

from bisect import bisect_left

def solve():
    N, K = map(int, input().split())
    Arr = list(map(int, input().split()))

    if K >= 3: 
        print(0)
        return 

    Arr.sort()
    ans = Arr[0]
    for i in range(1, N):
        ans = min(ans, Arr[i] - Arr[i - 1])
    
    if K == 1:
        print(ans)
        return 
    
    for i in range(0, N):
        for j in range(i + 1, N):
            diff = Arr[j] - Arr[i]
            index = bisect_left(Arr, diff)
            if index != N:
                ans = min(ans, Arr[index] - diff)
            if index != 0:
                ans = min(ans, diff - Arr[index - 1])
    
    print(ans)
            

    


for _ in range(int(input())):
    solve()