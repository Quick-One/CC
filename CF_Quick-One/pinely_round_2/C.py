from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    s = set(A)
    for i in range(0, N+1):
        if i not in s:
            MEX = i
            break
    
    A.append(MEX)

    pointer = (-K) % (N+1)
    # print(pointer)

    ans = []
    while len(ans) != N:
        ans.append(A[pointer])
        pointer += 1 
        pointer %= (N+1)
    print(*ans)


for _ in range(int(input())):
    solve()