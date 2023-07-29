from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    n,m, k,h = map(int, input().split())
    a = list(map(int, input().split()))

    ans = 0
    for i in a:
        diff = (h-i)
        if diff == 0:
            continue
        if diff % k == 0 and abs(diff) <= (m-1) * (k):
            ans += 1

    print(ans)
for _ in range(int(input())):
    solve()