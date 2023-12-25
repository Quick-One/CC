from sys import stdin
def input(): return stdin.readline()[:-1]

from collections import defaultdict

N = int(input())
strings = list(input().split())
A  = [dict() for _ in range(6)]
l = [[] for _ in range(6)]

for s in strings:
    key = len(s)
    l[key].append(s)
    key2 = sum(int(c) for c in s)
    if key2 in A[key]:
        A[key][key2] += 1
    else:
        A[key][key2] = 1

ANS = 0

def deal_case(i, j):
    ANS = 0
    if i == j:
        for val in A[i].values():
            ANS += val * val
    
    elif i > j:
        need = {}
        start = (i + j) // 2
        end = i - start
        for s in l[i]:
            v1 = sum(int(c) for c in s[:start])
            v2 = sum(int(c) for c in s[start:])
            need[v1 - v2] = need.get(v1 - v2, 0) + 1
        for key in need:
            if key in A[j]:
                ANS += need[key] * A[j][key]
    
    else:
        need = {}
        start = (i + j) // 2
        end = j - start
        for s in l[j]:
            v1 = sum(int(c) for c in s[:end])
            v2 = sum(int(c) for c in s[end:])
            need[v2 - v1] = need.get(v2 - v1, 0) + 1
        for key in need:
            if key in A[i]:
                ANS += need[key] * A[i][key]

    return ANS


for i in range(1, 6):
    for j in range(1, 6):
        if ( i + j )% 2 == 0:
            temp = deal_case(i, j)
            # print(i, j, temp)
            ANS += deal_case(i, j)

print(ANS)