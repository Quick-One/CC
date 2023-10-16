from sys import stdin
def input(): return stdin.readline()[:-1]
 

def to_important(city, l, K):
    if city < K:
        return 0
    ans = float('inf')
    for i in range(K):
        x,y = l[i]
        a,b = l[city]
        dist = abs(x-a) + abs(y-b)
        ans = min(ans, dist)
    return ans

def solve():
    N, K, a, b = map(int, input().split())
    l = []
    for _ in range(N):
        x,y = map(int, input().split())
        l.append((x,y))
    
    a-=1
    b-=1

    x1, y1 = l[a]
    x2, y2 = l[b]
    dist = abs(x1-x2) + abs(y1-y2)
    dist = min(dist, to_important(a, l, K) + to_important(b, l, K))
    print(dist)

for _ in range(int(input())):
    solve()
