from sys import stdin
def input(): return stdin.readline()[:-1]


A = [0] * (10 ** 6 + 1)
k = 2
while True:
    s = 1 + k + k*k
    if s > 10 ** 6:
        break
    A[s] = 1
    n = 3
    while True:
        s += k**n
        if s > 10 ** 6:
            break
        A[s] = 1
        n += 1
    k += 1

def solve():
    N = int(input())
    if A[N]:
        print('YES')
    else:
        print('NO')
    




for _ in range(int(input())):
    solve()