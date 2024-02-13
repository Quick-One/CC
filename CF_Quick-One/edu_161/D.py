from sys import stdin
def input(): return stdin.readline()[:-1]

from math import comb

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    D = list(map(int, input().split()))
    
    R = [i for i in range(1, N)] + [-1]
    L = [-1] + [i for i in range(0, N)]
    
    UN_STABLE_NODES = []
    for i in range(0, N):
        Atch = 0
        if L[i] != -1:
            Atch += A[L[i]]
        if R[i] != -1:
            Atch += A[R[i]]
        defense = D[i]
        if Atch > defense:
            UN_STABLE_NODES.append(i)

    ANS = []
    # print(UN_STABLE_NODES)
    dead = set()
    while True:
        # print(UN_STABLE_NODES)
        if len(UN_STABLE_NODES) == 0:
            break
        die = 0
        check = set()
        for i in UN_STABLE_NODES:
            dead.add(i)
            if L[i] != -1:
                R[L[i]] = R[i]
                check.add(L[i])
            if R[i] != -1:
                L[R[i]] = L[i]
                check.add(R[i])
            die += 1
        new_UN_STABLE_NODES = []
        ANS.append(die)
        for i in check:
            if i in dead:
                continue
            Atch = 0
            if L[i] != -1:
                Atch += A[L[i]]
            if R[i] != -1:
                Atch += A[R[i]]
            defense = D[i]
            if Atch > defense:
                new_UN_STABLE_NODES.append(i)
        UN_STABLE_NODES = new_UN_STABLE_NODES

    # count the number of connected components
    ANS += [0] * (N - len(ANS))
    print(*ANS)
            
        
    
for _ in range(int(input())):
    solve()