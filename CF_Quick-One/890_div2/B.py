from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():


    N = int(input())
    A = list(map(int, input().split()))
    A = [a-1 for a in A]
    if N == 1:
        print("NO")
        return
    
    alpha = 0
    c = A.count(0)
    for i in A:
        if i != 0:
            alpha += i
        if alpha >= c:
            print("YES")
            return
    print("NO")
    

for _ in range(int(input())):
    solve()