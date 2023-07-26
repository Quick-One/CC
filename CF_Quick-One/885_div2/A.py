from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N, M, K = map(int, input().split())
    x,y = map(int, input().split())

    ans = False
    for _ in range(K):
        x2,y2 = map(int, input().split())
        manhattan = abs(x2-x) + abs(y2-y)
        if manhattan % 2 == 0:
            ans = True
    ans = (not ans)
    if ans:
        print("YES")
    else:
        print("NO")


for _ in range(int(input())):
    solve()