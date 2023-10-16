from sys import stdin
def input(): return stdin.readline()[:-1]

def ceildiv(a, b):
    return -(a // -b)

from math import gcd
def isprime(n):
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return (False, i)
    return (True, None)


def solve():
    l,r = map(int, input().split())

    if 4<=l:
        if (l%2 == 0):
            print(l//2, l//2)
            return
        if (r-l+1) != 1:
            n = l+ 1
            print(n//2, n//2)
            return
        if (r-l+1) == 1:
            n = l
            a,b = isprime(n)
            if a:
                print(-1)
                return
            else:
                fact = b
                e = n // fact
                print(fact, (e-1)*fact)
                return
    else:
        if (l <= 4 <= r):
            print(2, 2)
            return
        for a in range(1, 7):
            for b in range(1, 7):
                s = a + b
                if l <= s <=r and gcd(a,b) != 1:
                    print(a, b)
                    return
        print(-1)
        return



for _ in range(int(input())):
    solve()