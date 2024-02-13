from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    X = int(input())
    binary_rep = list(bin(X)[2:])
    binary_rep = [int(x) for x in binary_rep]
    indices = [i for i in range(len(binary_rep))]
    indices.reverse()
    
    arr = []
    for i in range(len(binary_rep)-1):
        arr.append((i, 1, i))
    # print(binary_rep)
    INF = 10**8    
    for i in range(1, len(binary_rep)):
        if binary_rep[i]:
            arr.append((indices[i], 0, INF))
            INF += 1
    ANS = []
    arr.sort()
    
    for _, _, x in arr:
        ANS.append(x)
    print(len(ANS))
    print(* ANS)

for _ in range(int(input())):
    solve()