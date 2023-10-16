from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    XOR = 0
    for i in a:
        XOR = XOR ^ i
    ORB = 0
    for i in b:
        ORB = ORB | i
    XOR2 = 0
    for i in a:
        XOR2 = XOR2 ^ (i | ORB)
    
    if n % 2 == 0:
        print(XOR2, XOR)
    else:
        print(XOR, XOR2)

for _ in range(int(input())):
    solve()