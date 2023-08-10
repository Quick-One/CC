from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():



    N = int(input())
    

    
    arr = list(map(int, input().split()))

    if N == 1:
        print(1)
        return
    b = sorted(arr)
    
    d = {}
    for i in range(N):
        d[b[i]] = i

    ANS = [0] * N

    segments = [0] * (N-1)
    for i in range(N-1):
        segments[i] = b[i+1] - b[i]
    
    filter = [0] * (N-1)
    filter[0] = 2-N
    for i in range(1, N-1):
        filter[i] = filter[i-1] + 2
    initial = 0
    initial += N
    for i in range(N-1):
        initial += segments[i] * (N-1-i)
    ANS[0] = initial

    for i in range(1, N):
        ANS[i] = ANS[i-1] + (filter[i-1] * segments[i-1])
    
    # print(*ANS)
    a = []
    for i in arr:
        a.append(ANS[d[i]])
    print(*a)
    

for _ in range(int(input())):
    solve()