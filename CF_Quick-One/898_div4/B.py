from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N = int(input())
    a = list(map(int, input().split()))
    m = min(a)
    k = a.index(m)
    a[k] += 1

    ans = 1
    for i in a:
        ans *= i
    print(ans)

for _ in range(int(input())):
    solve()