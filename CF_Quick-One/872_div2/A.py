from sys import stdin
def input(): return stdin.readline()[:-1]


def solve():
    string = input().strip()
    N = len(string)

    if len(set(string)) == 1:
        print(-1)
    else:
        print(N-1)

for _ in range(int(input())):
    solve()