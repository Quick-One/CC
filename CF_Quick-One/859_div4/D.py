from sys import stdin
def input(): return stdin.readline()[:-1]

def oi():
    return int(input())
 
def ti():
    return map(int, input().split())
 
def mi():
    return list(map(int, input().split()))
 
def solve():
    N, Q = ti()
    arr = mi()
    prefix_sum = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]
        prefix_sum[i] %= 2
    # print(prefix_sum)
    s = prefix_sum[-1]
    s %= 2
    for _ in range(Q):
        l,r,k = ti()
        o = prefix_sum[r] - prefix_sum[l - 1]
        size = r - l + 1
        o %= 2
        size %= 2
        size *= k
        size %= 2
        ans = size - o + s
        ans %= 2
        if ans == 1:
            print("YES")
        else:
            print("NO")

    # print(prefix_sum)
    
for _ in range(oi()):
    solve()