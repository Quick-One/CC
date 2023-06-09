from heapq import heappush, heappop
from sys import stdin
def input(): return stdin.readline()[:-1]


def solve():
    s1 = list(input().strip())
    s2 = list(input().strip())
    s = [s1, s2]
    block, q = map(int, input().split())
    PQ = []

    size = len(s1)
    entropy = 0
    for i in range(size):
        if s1[i] != s2[i]:
            entropy += 1

    for t in range(1, q + 1):

        while PQ and PQ[0][0] <= t:
            _, index = heappop(PQ)
            entropy += (s[0][index] != s[1][index])

        query = list(map(int, input().split()))
        n = len(query)

        if n == 1:
            if entropy == 0:
                print('YES')
            else:
                print('NO')

        elif n == 2:
            index = query[1] - 1
            entropy -= (s[0][index] != s[1][index])
            heappush(PQ, (t + block, index))

        else:
            a, i1, b, i2 = query[1:]
            a -= 1
            b -= 1
            i1 -= 1
            i2 -= 1
            entropy -= (s[0][i1] != s[1][i1])
            entropy -= (s[0][i2] != s[1][i2])
            s[a][i1], s[b][i2] = s[b][i2], s[a][i1]
            entropy += (s[0][i1] != s[1][i1])
            entropy += (s[0][i2] != s[1][i2])


for _ in range(int(input())):
    solve()
