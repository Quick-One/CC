from sys import stdin
def input(): return stdin.readline()[:-1]

from collections import defaultdict

def get_bit_count(n):
    # returns the number of bits in the binary representation of n
    count = 0
    while n:
        count += 1
        n >>= 1
    return count

def solve():
    d = defaultdict(list)
    N = int(input())
    A = list(map(int, input().split()))

    for i in range(N):
        d[get_bit_count(i)].append(A[i])
    
    for v in d.values():
        n = len(v)
        for i in range(n-1):
            if v[i] > v[i + 1]:
                print("NO")
                return
    print("YES")

for _ in range(int(input())):
    solve()