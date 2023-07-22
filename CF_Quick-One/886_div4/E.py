from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N, C = map(int, input().split())
    A = list(map(int, input().split()))

    sigma = sum(A)
    sigma_square = sum([x*x for x in A])

    a = N
    b = sigma
    c = (sigma_square - C)/4

    D = b*b - 4*a*c
    root = (-b + D**0.5)/(2*a)

    print(round(root))

for _ in range(int(input())):
    solve()