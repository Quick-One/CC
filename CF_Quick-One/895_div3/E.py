from sys import stdin
def input(): return stdin.readline()[:-1]

from math import lcm

def solve():
    N = int(input())
    arr = list(map(int, input().split()))
    bin_string = input().strip()
    curr = 0

    for i in range(N):
        if bin_string[i] == '1':
            curr ^= arr[i]

    prefix_XOR = [0] * (N+1)
    for i in range(N):
        prefix_XOR[i+1] = prefix_XOR[i] ^ arr[i]
    ANS = []
    q = int(input())
    for _ in range(q):
        query = list(map(int, input().split()))
        if len(query) == 2:
            t, c = query
            if c == 1:
                ANS.append(curr)
            else:
                ANS.append(curr ^ prefix_XOR[N])
        else:
            _, l,r = query
            ## get XOR of [l,r] inclusive
            ans = prefix_XOR[r] ^ prefix_XOR[l-1]
            curr = curr ^ ans
    print(*ANS)

for _ in range(int(input())):
    solve()