from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    b.sort()
    z = list( zip(a, range(N)) )
    z.sort()
    indicies = [0] * N
    for i, v in enumerate(z):
        indicies[v[1]] = i
    # print(*indicies)  
    print(*[b[i] for i in indicies])

for _ in range(int(input())):
    solve()