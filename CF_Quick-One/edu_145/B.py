from sys import stdin
def input(): return stdin.readline()[:-1]

def oi():
    return int(input())
 
def ti():
    return map(int, input().split())
 
def mi():
    return list(map(int, input().split()))



def bin_search(N, low, high, f):
    # Finding the first element that has value greater than or equal to N
    while low < high:
        mid = (low + high) // 2
        if f(mid) < N:
            low = mid + 1
        else:
            high = mid
    return low


def solve():
    N = oi()
    n1 = bin_search(N, 1, 10**9, lambda x: 1 + 4 * (x*(x-1)))
    n2 = bin_search(N, 1, 10**9, lambda x: 4 * x * x)
    n1 = 2 * (n1 - 1)
    n2 = 2 * n2 - 1
    print(min(n1, n2))
    
    


for _ in range(oi()):
    solve()