from sys import stdin
def input(): return stdin.readline()[:-1]

MOD = 10**9 + 7

def inverse(x):
    return pow(x, MOD-2, MOD)


def nC2(n):
    INV2 = pow(2, MOD-2, MOD)
    x = n 
    x *= (n-1)
    x *= INV2
    return x % MOD

def solve():
    n, m , k = map(int, input().split())
    fi = []
    for _ in range(m):
        _, _, alpha = map(int, input().split())
        fi.append(alpha)
        
    combinations = nC2(n)
    inverse_combinations = inverse(combinations)
    
    const1 = combinations - m
    const1 *= inverse_combinations
    const1 %= MOD
    
    const2 = m
    const2 *= inverse_combinations
    const2 %= MOD 
    
    ANS = 0
    for i in fi:
        frac = i * k
        frac *= inverse_combinations
        frac %= MOD
        ANS += frac
    
    DP = [0] * (k+1)
    for i in range(1, k+1):
        new = 0
        new += const1 * DP[i-1]
        new %= MOD
        
        part2 = (k-i)*inverse_combinations
        part2 += DP[i-1]
        part2 %= MOD
        part2 *= const2
        part2 %= MOD
        new += part2
        new %= MOD
        DP[i] = new
        
    
    ANS += DP[k]
    ANS %= MOD
    print(ANS)
        
for _ in range(int(input())):
    solve()