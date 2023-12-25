from sys import stdin
def input(): return stdin.readline()[:-1]

def bin_count(n : int) -> int:
    ans = 0
    while n > 0:
        n >>= 1
        ans += 1
    return ans

def check(l, r):
    x,y = bin_count(l), bin_count(r)
    l = l << (32 - x)
    r = r << (32 - y)
    return r < l

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    
    ANS = 0
    previous = bin_count(A[0])

    for i in range(1, N):
        current = bin_count(A[i])
        
        if current > previous:
            previous = current
        else:
            boolean = check(A[i-1], A[i])
            new_height = previous + boolean
            ANS += new_height - current
            previous = new_height
    
    print(ANS)


for _ in range(int(input())):
    solve()