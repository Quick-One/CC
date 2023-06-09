from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N, K, temp = map(int, input().split())
    arr = list(map(int, input().split()))
    a = []
    l = []
    for i in arr:
        if i <= temp:
            l.append(i)
        else:
            a.append(l)
            l = []
    a.append(l)

    a = list(map(len, a))
    ans = 0
    for i in a:
        alpha = i - K + 1
        if alpha > 0:
            ans += (alpha * (alpha + 1)) // 2
    print(ans)
for _ in range(int(input())):
    solve()