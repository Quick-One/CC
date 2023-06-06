from sys import stdin
def input(): return stdin.readline()[:-1]

from math import gcd

def func(n ,e):
    k = 0
    while n % e == 0:
        n //= e
        k += 1
    if n == 1:
        return True, k
    else:
        return False, k


def solve():
    d, n = map(int, input().split())

    if d < n:
        print("NO")
        return

    if d == n:
        print("YES")
        return
    
    else:
        comomn = gcd(d, n)
        d //= comomn
        n //= comomn

        d1, d2 = func(d, 3)
        n1, n2 = func(n, 2)
        if d1 and n1 and d2 >= n2:
            print("YES")
        else:
            print("NO")

for _ in range(int(input())):
    solve()