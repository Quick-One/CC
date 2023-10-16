from sys import stdin
def input(): return stdin.readline()[:-1]

def ask(a):
    print('? {}'.format(a), flush=True)
    x = int(input())
    if x == -1: exit()
    return x

def answer(a):
    print('! {}'.format(a), flush=True)


def solve():
    N, K = map(int, input().split())
    qs = []
    for i in range(N//K):
        left = i*K+1
        right = (i+1)*K
        qs.append((left, right))
    
    ans = 0
    for a,b in qs:
        ans ^= ask(a)
    ask(qs[-1][0])

    if (N % K) != 0:
        diff = (N % K) // 2
        ans ^= ask( N - diff - K + 1)
        ans ^= ask( N - K + 1)

    answer(ans) 


for _ in range(int(input())):
    solve()