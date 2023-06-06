from sys import stdin
input=lambda :stdin.readline()[:-1]

def oi():
    return int(input())


def ti():
    return map(int, input().split())


def mi():
    return list(map(int, input().split()))
from math import gcd

def solve():
    N = int(input())
    s = input().strip()

    a = s[:N//2]
    b = s[-(N//2):][::-1]
    XOR_s = ''
    for i in range(N//2):
        XOR_s += str(int(a[i]) ^ int(b[i]))
    s = XOR_s.split('0')
    c = 0
    for i in s:
        if i:
            c += 1
    if c > 1:
        print("NO")
    else:
        print("YES")


for _ in range(oi()):
    solve()
