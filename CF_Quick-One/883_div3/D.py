from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N, D, H  = map(int, input().split())
    D /= 2

    ys = list(map(int, input().split()))
    ys.append(float('inf'))
    ans = 0
    for i in range(len(ys) - 1):
        h1 = ys[i]
        h2 = ys[i + 1]
        delta = h2 - h1
        x = min(H, delta)

        lower = D
        slope = D/H
        upper = D - slope * x
        height = x

        ans += (0.5) * (lower + upper) * height
    
    print(ans*2)

for _ in range(int(input())):
    solve()