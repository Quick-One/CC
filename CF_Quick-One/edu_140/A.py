def oi():
    return int(input())


def ti():
    return map(int, input().split())


def mi():
    return list(map(int, input().split()))


def solve():
    x = []
    y = []
    input()
    for _ in range(3):
        a, b = ti()
        x.append(a)
        y.append(b)
    if len(set(x)) == 3 or len(set(y)) == 3:
        print("YES")
    else:
        print("NO")



for _ in range(oi()):
    solve()
