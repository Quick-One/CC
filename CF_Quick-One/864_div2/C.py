from sys import stdin
def input(): return stdin.readline()[:-1]

def oi():
    return int(input())
 
def ti():
    return map(int, input().split())
 
def ask(a, b):
    print('? {} {}'.format(a, b), flush=True)
    return int(input())

def answer(a, b):
    print('! {} {}'.format(a, b), flush=True)

def solve():
    N, M = ti()
    d = ask(1, 1)
    X, Y = 1+d, 1+d
    if 0 < X <= N and 0 < Y <= M:
        d = ask(X, Y)
        if ask(X-d, Y) == 0: answer(X-d, Y)
        else: answer(X, Y-d)
    elif M > N: answer(N-ask(N, Y), Y)
    else: answer(X, M-ask(X, M))
    
for _ in range(oi()):
    solve()