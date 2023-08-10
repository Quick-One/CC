from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N = int(input())
    A = list(map(int, input().split()))

    d = []
    for i in A:
        d.append(i%2)
    
    if d.count(1) %2 == 0:
        print("YES")
    else:
        print("NO")
    

for _ in range(int(input())):
    solve()