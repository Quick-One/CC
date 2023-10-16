from sys import stdin
def input(): return stdin.readline()[:-1]

d = {}


def calc_score(i, j):
    i += 1
    j += 1

    x = abs(i - 5.5)
    y = abs(j - 5.5)
    k = max(x, y)

    alpha = round(k * 2)
    alpha -= 1
    alpha //= 2
    return 5 - alpha

    


def solve():
    A = []
    for _ in range(10):
        A.append(input().strip())
    
    s = 0
    for i in range(10):
        for j in range(10):
            if A[i][j] == 'X':
                s += calc_score(i, j)
    print(s)


for _ in range(int(input())):
    solve()