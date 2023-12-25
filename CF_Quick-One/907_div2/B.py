from sys import stdin
def input(): return stdin.readline()[:-1]

from collections import defaultdict

def solve():
    n, q = map(int, input().split())
    A = list(map(int, input().split()))
    X = list(map(int, input().split()))

    b = []
    highest = 40
    for i in X:
        if i < highest:
            highest = i
            b.append(highest)
    # print(b)
    for x in range(len(A)):
        for j in b:
            if A[x] % (2 ** j) == 0:
                A[x] += (2 ** (j-1))
    print(*A)

    
for _ in range(int(input())):
    solve()