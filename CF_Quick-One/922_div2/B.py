from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B= list(map(int, input().split()))
    C = list(zip(A, B))
    C.sort()
    ANS1 = []
    ANS2 = []
    for y, x in C:
        ANS2.append(y)
        ANS1.append(x)
    print(*ANS2)
    print(*ANS1)
    
for _ in range(int(input())):
    solve()