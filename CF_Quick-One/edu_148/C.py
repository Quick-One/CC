from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N  = int(input())
    A  = list(map(int, input().split()))

    if N == 1:
        print(1)
        return

    diff = [0] * (N-1)
    for i in range(N-1):
        diff[i] = A[i+1] - A[i]
    
    l = sum(map(abs, diff))
    if l == 0:
        print(1)
        return
    e = [i for i in diff if i != 0]
    e = [i//abs(i) for i in e]
    c = 0
    for i in range(len(e)-1):
        if e[i] != e[i+1]:
            c += 1
    print(c+2)

for _ in range(int(input())):
    solve()