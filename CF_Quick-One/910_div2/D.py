from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    mini = []
    for i in range(N):
        mini.append(min(A[i], B[i]))
    m = max(mini)

    defa = 0
    for i in range(N):
        defa += abs(A[i] - B[i])
    
    ANS = defa
    for a,b in zip(A, B):
        beta=max(a, b)

        if beta < m:
            ANS = max(ANS, defa + 2 * (m - beta))
        

    print(ANS)


for _ in range(int(input())):
    solve()