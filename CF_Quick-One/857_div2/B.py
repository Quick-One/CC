def oi():
    return int(input())
 
def ti():
    return map(int, input().split())
 
def mi():
    return list(map(int, input().split()))

from math import ceil
def f(n):
    if n==0:
        return 0
    else:
        return ceil((n+1)/2)
def solve():
    n = oi()
    a = mi()

    defined = 0
    undef = 0
    ans = 0
    for i in a:
        if i == 1:
            undef += 1
            ans = max(f(defined)+undef, ans)
        else:
            defined += undef
            undef = 0
            ans =  max(f(defined), ans)
        # print(undef, defined)
    print(ans)


for _ in range(oi()):
    solve()