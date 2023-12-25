from sys import stdin
def input(): return stdin.readline()[:-1]

N = int(input())
A = list(map(int, input().split()))

B = [0] * (N)
for i in range(N-1):
    B[i+1] = B[i] ^ A[i]

XOR = 0
total_bits = len(bin(2 * N)) - 2
for i in range(total_bits + 1):
    arr = [(a>>i)&1 for a in B]
    if N < 2 * sum(arr):
        XOR |= 1 << i

B = [i ^ XOR for i in B]
print(*B)