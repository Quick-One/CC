from sys import stdin
def input(): return stdin.readline()[:-1]


def ceildiv(a, b):
    return -(a // -b)

def func(x,g):
    r = x % g
    if r >= ceildiv(g, 2):
        return x + (g - r)
    else:
        return x - r

def solve():
    N, K, G = map(int, input().split())

    loss = ceildiv(G, 2) - 1

    total = K * G
    total -= (N-1) * loss
    if total <= 0:
        print(K*G)
    else:
        final = func(total, G)  
        print(K*G - final)


for _ in range(int(input())):
    solve()