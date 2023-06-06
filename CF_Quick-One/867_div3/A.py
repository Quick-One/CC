from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    ans = -1
    ans_index = -2
    for i in range(N):
        cost = i + A[i]
        if cost <= T:
            if B[i] > ans:
                ans = B[i]
                ans_index = i
    print(ans_index + 1)
    

for _ in range(int(input())):
    solve()