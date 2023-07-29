from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    if N == 1:
        print("YES")
        return
    
    if [A[0]] == [A[-1]]:
        if A.count(A[0]) >= K:
            print("YES")
            return
        

    d = {}
    for i in range(N):
        if A[i] in d:
            d[A[i]].append(i+1)
        else:
            d[A[i]] = [i+1]
    
    a = d[A[0]]
    b = d[A[-1]]
    if len(a) >= K:
        start = a[K-1]
    else:
        print("NO")
        return
    if len(b) >= K:
        end = b[-K]
    else:
        print("NO")
        return 
    if start < end:
        print("YES")
    else:
        print("NO")
for _ in range(int(input())):
    solve()