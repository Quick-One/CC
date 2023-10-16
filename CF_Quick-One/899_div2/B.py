from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N = int(input())
    a = []

    for _ in range(N):
        l = list(map(int, input().split()))
        a.append(l[1:])

    state = [0] * (51)
    for s in a:
        for i in s:
            state[i] = 1
    kappa = sum(state)

    ans = 0
    for k in range(1, 51):
        state = [0] * (51)
        for s in a:
            if k not in s:
                for i in s:
                    state[i] = 1
        lo = sum(state)
        if kappa == lo:
            continue
        ans = max(ans, sum(state))
    print(ans)

    

for _ in range(int(input())):
    solve()