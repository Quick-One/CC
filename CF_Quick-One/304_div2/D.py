from sys import stdin, stdout
def input(): return stdin.readline()[:-1]

LIMIT = 5_000_001

SEIVE = [0] * LIMIT
for i in range(2, LIMIT):
    if SEIVE[i] == 0:
        cnt = 1 
        for j in range(i, LIMIT, i):
            SEIVE[j] = 1 + SEIVE[cnt] 
            cnt += 1
for i in range(2, LIMIT):
    SEIVE[i] += SEIVE[i - 1]


ANS = []
for _ in range(int(input())):
    a, b = map(int, input().split())
    ANS.append(SEIVE[a] - SEIVE[b])

stdout.write('\n'.join(map(str, ANS)))