from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N = int(input())
    s = input().strip()
    c = set(s)

    if len(c) != 1:
        print('YES')
    else:
        l = s[0]
        if l == '0':
            print('YES')
        else:
            print('NO')


for _ in range(int(input())):
    solve()