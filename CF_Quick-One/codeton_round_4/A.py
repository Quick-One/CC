# Source: https://usaco.guide/general/io

def solve():
    N = int(input())
    arr = list(map(int, input().split()))

    for i, x in enumerate(arr,1):
        if i >=x:
            print("YES")
            return

    print("NO")

t = int(input())
for _ in range(t):
    solve()