from sys import stdin
def input(): return stdin.readline()[:-1]
import sys


from math import sqrt
UP = 10 ** 6 + 1
anses = []

def factorize(n) -> list:
    if n == 1: return []
    c, ans = 2, [n]
    while (c * c < n):
        if n % c == 0:
            ans.extend([c, n // c])
        c += 1
 
    if c * c == n: ans.append(c)
    return ans

def solve():
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    d = {}
    for i in arr:
        if i not in d:
            d[i] = 0
        d[i] += 1

    ans = 0
    for v in d.values():
        ans += v * (v-1) * (v-2)

    const_a = pow(arr[-1], 2/3) + 5
    const_b = int(pow(arr[-1], 1/3)) + 5
    for s in d.keys():
        if s <= const_a:
            for f in factorize(s):
                s1 = s // f
                s3 = s * f

                if s1 in d and s3 in d:
                    ans += d[s] * d[s1] * d[s3]
        else:
            for f in range(2, const_b):
                e3 = s * f
                if e3 > arr[-1]:
                    break
                if s % f == 0:
                    s1 = s // f
                    if s1 in d and e3 in d:
                        ans += d[s] * d[s1] * d[e3]
    anses.append(ans)


    
for _ in range(int(input())):
    solve()

sys.stdout.write('\n'.join(map(str, anses)))