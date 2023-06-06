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
    arr = mi()

    # iteratere over all pairs
    for i in range(N):
        for j in range(i+1, N):
            if gcd(arr[i], arr[j]) <=2:
                print("YES")
                return
    print("NO")
    

for _ in range(oi()):
    solve()
