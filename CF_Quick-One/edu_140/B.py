def oi():
    return int(input())


def ti():
    return map(int, input().split())


def mi():
    return list(map(int, input().split()))

def ceildiv(a, b):
    return -(a // -b)

def solve():
    n = oi()
    a = mi()
    ans = a[0]
    a = a[1:]
    a.sort()
    for i in a:
        if ans < i:
            ans = ceildiv(ans + i, 2)
    print(ans)


for _ in range(oi()):
    solve()
