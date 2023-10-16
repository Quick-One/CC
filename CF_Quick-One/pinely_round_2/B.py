from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N = int(input())
    A = list(map(int, input().split()))

    ans = 0
    d = {}
    for i, j in enumerate(A):
        d[j] = i
    
    for i in range(1, N):
        if d[i+1] < d[i]:
            ans += 1
    print(ans)

for _ in range(int(input())):
    solve()