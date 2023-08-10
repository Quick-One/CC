from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    C = [0] * N
    for i in range(N):
        C[i] = A[i] - B[i]
    
    D = list(zip(C, range(N)))
    D.sort()

    x = D[-1][0]
    ans = []
    for i in D:
        if i[0] == x:
            ans.append(i[1]+1)
    print(len(ans))
    print(*ans)
    

for _ in range(int(input())):
    solve()