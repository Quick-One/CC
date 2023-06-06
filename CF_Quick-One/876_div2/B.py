from sys import stdin
def input(): return stdin.readline()[:-1]

from collections import defaultdict

def solve():
    N = int(input())
    A = []
    B = []
    for _ in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    
    # print(A)
    # print(B)

    indexes = list(range(N))
    indexes.sort(key=lambda i: B[i], reverse=True)

    A = [A[i] for i in indexes]
    B = [B[i] for i in indexes]

    d = defaultdict(list)
    for i in range(N):
        d[A[i]].append(B[i])

    ans = 0
    for key, val in d.items():
        ans += sum(val[:key])
    print(ans)


for _ in range(int(input())):
    solve()