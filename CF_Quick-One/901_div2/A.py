from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    a,b,n = map(int, input().split())
    arr=  list(map(int, input().split()))

    # arr.sort()
    ans = b
    for i in arr:
        ans += min(a-1, i)
    print(ans)
for _ in range(int(input())):
    solve()