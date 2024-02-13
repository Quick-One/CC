from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N, K = map(int, input().split())
    ANS = list(range(1, N+1))[::-1]
    ANS[-K-1:] = ANS[-K-1:][::-1]
    print(*ANS)
    
    
for _ in range(int(input())):
    solve()