from sys import stdin
def input(): return stdin.readline()[:-1]

N = int(input())
A = list(map(int, input().split()))

MOD = 998244353

ANS = 0

# (N+1)x2x2 with 0 dp

for dig_i in range(30):
    a = [(i >> dig_i) & 1 for i in A]
    a0, a1 = 0, 0
    b0, b1 = 0, 0
    s = 0
    for i in a:
        if i:
            B0, B1 = (a0 + a1) + 1, a1 + 1
            A0, A1 = b0 + b1,  b1
        else:
            A0, A1 = (a0 + a1) + 1, a1 + 1
            B0, B1 = b0 + b1,  b1
        
        A0 %= MOD
        B0 %= MOD

        a0, a1 = A0, A1
        b0, b1 = B0, B1
    
        s += B0
        s %= MOD
    ANS += s * (1<<dig_i)
    ANS %= MOD

print(ANS)
