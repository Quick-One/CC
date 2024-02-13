from sys import stdin
def input(): return stdin.readline()[:-1]
 
from math import gcd

def get_all_factors(n):
    factors = set()
    for i in range(1, int(n**0.5) + 3):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
    return sorted(factors)
 
def check(arr, k):
    ans = 0
    for i in range(k):
        for j in range(i, len(arr) - k, k):
            ans = gcd(ans, arr[j+k] - arr[j])
    return ans != 1

def solve():
    N = int(input())
    Arr = list(map(int, input().split()))
    
    facs = get_all_factors(N)
    ANS = 0
    for i in facs:
        if check(Arr, i):
            ANS += 1
    print(ANS)
        
    
for _ in range(int(input())):
    solve()