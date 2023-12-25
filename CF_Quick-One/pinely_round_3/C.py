from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N = int(input())
    L = list(map(int, input().split()))
    R = list(map(int, input().split()))
    cost = list(map(int, input().split()))

    a = []
    for i in range(N):
        a.append(L[i]<<1)
        a.append((R[i]<<1)+1)
    a.sort()
    
    stack = []
    arr = []

    for i in a:
        if (i&1):
            arr.append((i>>1) - stack.pop())
        else:
            stack.append(i>>1)
    
    arr.sort()
    cost.sort(reverse=True)

    ans = 0
    for i, j in zip(arr, cost):
        ans += i*j
    print(ans)
    

for _ in range(int(input())):
    solve()