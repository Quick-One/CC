from sys import stdin
def input(): return stdin.readline()[:-1]


def solve():
    N  = int(input())
    A = list(map(int, input().split()))

    tuples = [(A[i], i) for i in range(N)]
    tuples.sort()

    current = N
    ANS = [0] * N
    for i in tuples:
        _, index = i
        ANS[index] = current
        current -= 1
    print(*ANS)

for _ in range(int(input())):
    solve()