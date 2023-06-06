from collections import defaultdict

def one_input():
    return int(input())

def two_input():
    return map(int, input().split())

def many_input():
    return list(map(int, input().split()))

def solve():
    n = one_input()
    arr = many_input()
    arr.sort()
    d = defaultdict(int)
    for i in arr:
        d[i] += 1
    d = list(d.items())
    
    ans = 0
    for i in range(1, len(d)):
        if d[i][0] != d[i-1][0] + 1:
           ans += d[i-1][1]
        else:
            if d[i][1] < d[i-1][1]:
                ans += d[i-1][1] - d[i][1]
    ans += d[-1][1]
    print(ans)
                 
for _ in range(one_input()):
    solve()