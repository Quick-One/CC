def oi():
    return int(input())


def ti():
    return map(int, input().split())


def mi():
    return list(map(int, input().split()))

s = "FBFFBFFB"
def func(s):
    l = []
    s = s+s+s
    for i in range(0, 10):
        l.append(s[i:i+10])
    return l
L = func(s)

def solve():
    n = oi()
    string = input().strip()
    for i in L:
        if string in i:
            print("YES")
            return
    print("NO")

for _ in range(oi()):
    solve()
