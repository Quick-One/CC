def oi():
    return int(input())
 
def ti():
    return map(int, input().split())
 
def mi():
    return list(map(int, input().split()))
 
def solve():
    n, m =  ti()
    n = abs(n)
    m = abs(m)

    if n == m:
        print(2 * n)
        return
    else:
        print(2 * max(n, m) - 1)
        return
    
for _ in range(oi()):
    solve()