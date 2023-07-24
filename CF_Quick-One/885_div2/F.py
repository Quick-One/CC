from sys import stdin
def input(): return stdin.readline()[:-1]


N = int(input())
A = list(map(int, input().split()))

def convolve(arr, val):
    return [arr[i] ^ arr[(i+val)%N] for i in range(N)]

def check_all_zeros(arr):
    for i in arr:
        if i != 0:
            return False
    return True

if check_all_zeros(A):
    print(0)
    exit()

increment = N // 2
ans = 0

while increment != 0:
    new_state = convolve(A, increment)
    if not check_all_zeros(new_state):
        ans += increment
        A = new_state
    increment //= 2

print(ans+1)