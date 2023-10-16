from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N = int(input())
    arr = list(map(int, input().split()))   

    s = set(arr)
    if len(s) == 1:
        print(-1)
        return

    m = max(arr)
    k = arr.count(m)

    b = [m] * k
    c = [i for i in arr if i != m]
    print(len(c), len(b))
    print(*c)
    print(*b)

for _ in range(int(input())):
    solve()