from sys import stdin
def input(): return stdin.readline()[:-1]
 
 
MAXN = 10 ** 7 + 5
sieve = list(range(MAXN))
 
for i in range(2, MAXN):
    if sieve[i] == i:
        for j in range(i * i, MAXN, i):
            if sieve[j] == j:
                sieve[j] = i
 
def factorize(n):
    res = []
    while n != 1:
        res.append(sieve[n])
        n //= sieve[n]
    return res
 
 
def solve():
    N = int(input())
    arr = list(map(int, input().split()))
    d = {}
    for a in arr:
        for factor in factorize(a):
            d[factor] = d.get(factor, 0) + 1
    
    ans = 0
    b = 0
    for prime in d:
        alpha, beta = divmod(d[prime], 2)
        ans += alpha
        b += beta
    
    ans += b//3
    print(ans)
 
 
 
for _ in range(int(input())):
    solve()