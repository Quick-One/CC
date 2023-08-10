from sys import stdin
def input(): return stdin.readline()[:-1]

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

PROD = [0] * N
for i in range(N):
    PROD[i] = A[i] * B[i]

prefix_sum = [0] * (N)
prefix_sum[0] = PROD[0]
for i in range(1, N):
    prefix_sum[i] = prefix_sum[i - 1] + PROD[i]

suffix_sum = [0] * (N)
suffix_sum[-1] = PROD[-1]
for i in range(N - 2, -1, -1):
    suffix_sum[i] = suffix_sum[i + 1] + PROD[i]

ans = sum(PROD)

for r in range(1, N):
    R = r
    L = R - 1
    middle = 0
    while True:
        if L < -1:
            break
        elif L == -1:
            left_sum = 0
        else:
            left_sum = prefix_sum[L]
        
        if R == N:
            right_sum = 0
        elif R > N:
            break
        else:
            right_sum = suffix_sum[R]

        ans = max(ans, left_sum + middle + right_sum)
        if L == -1:
            break
        if R == N:
            break

        middle += A[L] * B[R] + A[R] * B[L]
        L -= 1
        R += 1

for r in range(2, N):
    R = r
    L = R - 2
    middle = PROD[r - 1]

    while True:
        if L < -1:
            break
        elif L == -1:
            left_sum = 0
        else:
            left_sum = prefix_sum[L]
        
        if R == N:
            right_sum = 0
        elif R > N:
            break
        else:
            right_sum = suffix_sum[R]
        ans = max(ans, left_sum + middle + right_sum)
        if L == -1:
            break
        if R == N:
            break
        middle += A[L] * B[R] + A[R] * B[L]
        L -= 1
        R += 1

print(ans)
