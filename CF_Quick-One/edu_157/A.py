from sys import stdin
def input(): return stdin.readline()[:-1]


def solve():
    x, y, K = map(int, input().split())
    if y < x:
        print(x)
    else:
        # ANS = y + y - x
        if x + K >= y:
            print(y)
            ANS = y
        else:
            print( y - x - K + y)
            

for _ in range(int(input())):
    solve()