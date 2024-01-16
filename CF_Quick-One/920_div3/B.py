from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N = int(input())
    s1 = input().strip()
    s2 = input().strip()
    a = 0
    b = 0
    for i, j in zip(s1, s2):
        if i == '1' and j == '0':
            a += 1
        elif i == '0' and j == '1':
            b += 1
    print( a + b - min(a, b) )
for _ in range(int(input())):
    solve()