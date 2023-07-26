from sys import stdin
def input(): return stdin.readline()[:-1]

def process(a,b):
    moves = 1

    while a != 0 and b != 0:
        invert = False
        if a > b:
            a,b = b,a
            invert = True
        
        k = b//a

        # Case 1 k >= 2
        if k >= 2:
            d,r = divmod(b, 2*a)
            moves += 3 * d
            a,b = a,r

            if invert:
                a,b = b,a
        
        # Case 2 k == 1
        else:
            if invert:
                a, b = b, a
            moves += 1
            a,b = b, abs(a-b)
        
    if a != 0:
        moves += 1
    
    return moves % 3


def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    C = []
    D = []
    for a, b in zip(A, B):
        if a == b == 0:
            continue
        C.append(process(a,b))
    if len(set(C)) <= 1:
        print("YES")
    else:
        print("NO")


for _ in range(int(input())):
    solve()