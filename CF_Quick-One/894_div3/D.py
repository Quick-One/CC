from sys import stdin
def input(): return stdin.readline()[:-1]


def NC2(n):
    return n * (n - 1) // 2 

def solve():
    N = int(input())

    lo = 2
    hi = 10 ** 18

    while (lo < hi):
        mid = lo + (hi - lo + 1)//2
        if not (N >= NC2(mid)):
            hi = mid - 1
        else:
            lo = mid
            
    # print(lo)
    ans = N - NC2(lo)
    ans += lo
    print(ans)  


for _ in range(int(input())):
    solve()