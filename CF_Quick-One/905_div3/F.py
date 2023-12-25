from sys import stdin
def input(): return stdin.readline()[:-1]

from collections import defaultdict

def solve():
    N = int(input())
    A = list(map(int, input().split()))

    d = defaultdict(list)
    for i, j in enumerate(A):
        d[j].append(i)

    changed = [0] * N
    for key, val in d .items():
        changed[val[0]] = key
        changed[val[-1]] = key

    m = {}
    for i, j in enumerate(changed):
        if j not in m:
            m[j] = 0
        m[j] += 1

    if 0 in m:
        del m[0]
    
    ANS = 0
    done = set()
    for i in range(N):
        num = changed[i]
        # print(i, num, "WOW")
        if num == 0:
            continue
        if num in done:
            m[num] -= 1
            if m[num] == 0:
                del m[num]
            continue
        done.add(num)
        m[num] -= 1
        if m[num] == 0:
            del m[num]
        # print(m)
        ANS += len(m)
        # print(i, ANS)

    # print(ANS)
    for v in d.values():
        if len(v) == 1:
            ANS += 1

    print(ANS)

    

for _ in range(int(input())):
    solve()