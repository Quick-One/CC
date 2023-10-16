from sys import stdin
def input(): return stdin.readline()[:-1]

N  = int(input())
A = list(map(int, input().split()))
A.sort()
l,r = 0, N-1

ans = 0
while (l < r):
    left, right = A[l], A[r]
    ans += (left + right) ** 2
    l += 1
    r -= 1

print(ans)