from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N = int(input())
    ANS = set()
    s = set()
    A = list(map(int, input().split()))
    
    s.add(A[0])
    ANS.add(A[0])
    
    for i in range(1, N):
        
        temp = set()
        for j in s: temp.add(j | A[i])
        temp.add(A[i])
        
        ANS |= temp
        s = temp
    
    # print(ANS)
    print(len(ANS))
    
solve()
    