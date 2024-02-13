from sys import stdin
def input(): return stdin.readline()[:-1]


mod = 998244353
MAXN = 10 ** 6
fact = [1] * (2 * MAXN + 10)
for i in range(1, 2 * MAXN + 10):
    fact[i] = (fact[i - 1] * i) % mod
    
def inv(x):
    return pow(x, mod - 2, mod)

def nCr(n, r):
    numerator = fact[n]
    denominator = (fact[r] * fact[n - r]) % mod
    return (numerator * inv(denominator)) % mod

def solve():
    c1, c2, c3 ,c4 = map(int, input().split())
    # case 1: c1 = c2
    ans = None
    if c1 == c2:
        if (c1 == c2 == 0):
            if (c3 > 0 and c4 > 0):
                ans = 0
            else:
                ans = 1
        else:
            e = c1
            # case 1 sequence starts with 1
            slot4 = e + 1
            slot3 = e
            q4 = nCr(slot4 + c4 - 1, c4)
            q3 = nCr(slot3 + c3 - 1, c3)
            ans = (q3 * q4) % mod
            # case 2 sequence starts with 2
            slot4 = e
            slot3 = e + 1
            q4 = nCr(slot4 + c4 - 1, c4)
            q3 = nCr(slot3 + c3 - 1, c3)
            ans += (q3 * q4) % mod
            ans %= mod
            
    elif abs(c1 - c2) == 1:
        e = max(c1, c2)
        q3 = nCr(e + c3 - 1, c3)
        q4 = nCr(e + c4 - 1, c4)
        ans = (q3 * q4) % mod
    
    else:
        ans = 0
    print(ans)

for _ in range(int(input())):
    solve()