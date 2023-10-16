from sys import stdin
def input(): return stdin.readline()[:-1]

def ceildiv(a, b):
    return -(a // -b)

def solve():
    a,b=  map(int, input().split())
    N = int(input())
    Arr = list(map(int, input().split()))
    s = sum(Arr)
    
    DP = [False] * (sum(Arr) + 1 )
    DP[0] = True

    for element in Arr:
        for i in range(len(DP), -1, -1):
            if i - element >= 0:
                if DP[i - element]:
                    DP[i] = True
    # print(DP)
    ans = []
    for sigma in range(len(DP)):
        if DP[sigma]:
            ans.append(max(ceildiv(sigma, a), ceildiv(s-sigma, b)))
    print(min(ans))

for _ in range(int(input())):
    solve()