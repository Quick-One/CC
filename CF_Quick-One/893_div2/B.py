from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N, M, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = A.copy()
    isOne = False
    if 1 in B:
        isOne = True
        B.remove(1)
    B.sort()
    B.insert(0, 1)
    B.append(N+1)
    
    d = {}
    for i in range(1, len(B)-1):
        d[B[i]] = (B[i-1], B[i+1])
    
    temp = M + 1
    if isOne:
        temp -= 1
    for i in range(1, len(B)):
        temp += (B[i] - B[i-1] - 1) // K
    ans_array = []
    for i, j in d.items():
        x,y = j
        aage = (i - x - 1) // K
        peeche = (y - i - 1) // K
        ans_array.append(temp - aage - peeche + (y-x-1)//K - 1)
    if isOne:
        ans_array.append(temp)
    ANS = min(ans_array)
    print(ANS, ans_array.count(ANS))


for _ in range(int(input())):
    solve()