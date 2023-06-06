def oi():
    return int(input())

def ti():
    return map(int, input().split())

def mi():
    return list(map(int, input().split()))

def solve():
    s = oi()
    arr = mi()

    n = 0
    for i in arr:
        if i < 0:
            n += 1
    n = n%2
    absolute = [abs(i) for i in arr]
    if n == 0:
        print(sum(absolute))
    else:

        print(sum(absolute) - 2*min(absolute))
    
for _ in range(oi()):
    solve()