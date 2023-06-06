def oi():
    return int(input())
 
def ti():
    return map(int, input().split())
 
def mi():
    return list(map(int, input().split()))
 
def solve():
    mod, s, p = ti()
    for i in range(1, min(p, 2*mod)+1):
        q = i * (i + 1)
        q //= 2
        if ((s + q) % mod) == 0:
            print('YES')
            return
    print('NO')

for _ in range(oi()):
    solve()