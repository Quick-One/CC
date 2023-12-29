from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    a,b,c = map(int, input().split())
    print(a ^ b ^ c)

for _ in range(int(input())):
    solve()