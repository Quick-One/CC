from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N, Q = map(int, input().split())

    for i in range(1, N):
        print(i, i+1)

    a = [2] + [i for i in range(3, N+1)]
    b = [2] + []

    for _ in range(Q):
        q = int(input())

        if q == len(a) or q == len(b):
            u, v1, v2 = -1, -1, -1
        elif q > len(a):
            required = q - len(a)
            u, v1, v2 = b[-required], b[-required-1], a[-1]  
            a.extend(b[-required:])
            b = b[:-required]
        else:
            required = len(a) - (q)
            u, v1, v2 = a[-required], a[-required-1], b[-1]
            b.extend(a[-required:])
            a = a[:-required]
        print(u, v1, v2)


for _ in range(int(input())):
    solve()