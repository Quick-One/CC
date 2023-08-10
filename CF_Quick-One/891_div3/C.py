from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = []
    for i in range(N-1):
        i += 1
        s = i * (i + 1) // 2
        s -= 1
        ans.append(A[s])
    ans.append(max(A))
    print(*ans)

for _ in range(int(input())):
    solve()