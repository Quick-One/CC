from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    groups = []
    prev = [A[0]]
    for i in range(1, len(A)):
        if (A[i] - prev[-1]) <= K:
            prev.append(A[i])
        else:
            groups.append(prev)
            prev = [A[i]]
    groups.append(prev)
    print(N - len(max(groups, key=len)))


for _ in range(int(input())):
    solve() 