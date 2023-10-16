from sys import stdin
def input(): return stdin.readline()[:-1]

from collections import deque

def calculate(arr, K):
    ans = 0
    s = 0
    l = 0
    for r in range(len(arr)):
        s += arr[r]
        while (s > K):
            s -= arr[l]
            l += 1
        ans = max(ans, r-l+1)
    return ans

def solve():
    N , K = map(int, input().split())
    A = list(map(int, input().split()))
    H = list(map(int, input().split()))

    alpha = []
    temp = [A[0]]
    for i in range(1, N):
        if (H[i-1] % H[i] == 0):
            temp.append(A[i])
        else:
            alpha.append(temp)
            temp = [A[i]]
    alpha.append(temp)
    # print(alpha)
    ans = 0
    for arr in alpha:
        ans = max(ans, calculate(arr, K))
    print(ans)




for _ in range(int(input())):
    solve()