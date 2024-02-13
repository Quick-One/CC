from sys import stdin
def input(): return stdin.readline()[:-1]

from math import comb

def solve():
    N = int(input())
    ARR = list(map(int, input().split()))
    dist_forward = []
    dist_backward = []
    dist_forward.append(1)
    
    for i in range(1, N - 1):
        piche = ARR[i] - ARR[i - 1]
        aage = ARR[i + 1] - ARR[i]
        piche =abs(piche)
        aage = abs(aage)
        if aage < piche:
            dist_forward.append(1)
        else:
            dist_forward.append(aage)
        
    dist_backward.append(1)
    for i in range(N-2, 0, -1):
        piche = ARR[i] - ARR[i - 1]
        aage = ARR[i + 1] - ARR[i]
        piche =abs(piche)
        aage = abs(aage)
        if piche < aage:
            dist_backward.append(1)
        else:
            dist_backward.append(piche)
    dist_backward.reverse()
    
    # print(* dist_forward)
    # print(* dist_backward)
    for i in range(1, N-1):
        dist_forward[i] += dist_forward[i-1]
        dist_backward[i] += dist_backward[i-1]
        
    def query_forward(l, r):
        if l == 0:
            return dist_forward[r]
        else:
            return dist_forward[r] - dist_forward[l - 1]
    
    def query_backward(l, r):
        if l == 0:
            return dist_backward[r]
        else:
            return dist_backward[r] - dist_backward[l - 1]
    
    Q = int(input())
    ANS = []
    for _ in range(Q):
        a, b = map(int, input().split())
        if a < b:
            l = a - 1
            r = a + ( b - a - 2)
            ans = query_forward(l, r)
            # print(l, r, ans)
            ANS.append(query_forward(l, r))
        else:
            l = b -1
            r = b + (a - b - 2)
            ans = query_backward(l, r)
            # print(l, r, ans)
            ANS.append(query_backward(l, r))
    print('\n'.join(map(str, ANS)))

for _ in range(int(input())):
    solve()