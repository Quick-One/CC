from sys import stdin
def input(): return stdin.readline()[:-1]

def case1(l, r, a, M):
    if l == 0:
        return -1
    l -= 1
    if M in a:
        non_last = len(a) - 1
    else:
        non_last = len(a)
    return min(M-1, l + non_last) + 1

def case2(l, r, a, M):
    if r == 0:
        return -1
    r -= 1
    if 1 in a:
        non_one = len(a) - 1
    else:
        non_one = len(a)
    
    return min(M-1, r + non_one) + 1

def case3(l, r, a, M):
    K = len(a)
    if K == 0:
        return -1
    ans = -1
    for i, x in enumerate(a):
        piche = i
        aage = K - i - 1
        piche_spaces = (x-1) - 1 + 1
        aage_spaces = (M - 1 - piche_spaces)
        # print(piche, aage, piche_spaces, aage_spaces)
        ans = max(ans, min(piche + l, piche_spaces) + min(aage + r, aage_spaces) + 1)
    return ans


def solve():
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    l = 0
    r = 0
    a = []
    for i in arr:
        if i == -1:
            l += 1
        elif i == -2:
            r += 1
        else:
            a.append(i)
    a = set(a)
    a = sorted(a)
    
    ans = max(case1(l, r, a, M), case2(l, r, a, M), case3(l, r, a, M))
    print(ans)

for _ in range(int(input())):
    solve()