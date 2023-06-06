from sys import stdin
def input(): return stdin.readline()[:-1]


def solve():
    N = int(input())
    d = {}
    for _ in range(N):
        a,b = map(int,input().split())
        if b not in d:
            d[b] = a
        else:
            d[b] = min(d[b],a)
    
    all1 = float('inf')
    if 11 in d:
        all1 = d[11]

    ans2 = float('inf')
    if 1 in d and 10 in d:
        ans2 = d[1] + d[10]
    
    ans3 = min(all1,ans2)
    if ans3 == float('inf'):
        print(-1)
    else:
        print(ans3)
for _ in range(int(input())):
    solve()