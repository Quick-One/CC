from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    a, b = map(int, input().split())
    print(a * (b//2))
    
for _ in range(int(input())):
    solve()