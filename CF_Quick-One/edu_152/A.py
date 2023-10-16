from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    b ,c, h = map(int, input().split())
    a = c + h
    if c + h + 1 <= b:
        print(c + h + 1 + c + h)
    else:
        print(b + b - 1)


for _ in range(int(input())):
    solve()