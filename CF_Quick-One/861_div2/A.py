from sys import stdin
def input(): return stdin.readline()[:-1]


def f(n):
    n = str(n)
    max_d = int(max(n))
    min_d = int(min(n))
    return max_d-min_d
    


def solve():
    l,u = map(int,input().split())

    Hundreds = l//100
    n1 = Hundreds*100 + 9
    n2 = Hundreds*100 + 90

    if l <= n1 <= u:
        if f(n1) == 9:
            print(n1)
            return
    
    if l <= n2 <= u:
        if f(n2) == 9:
            print(n2)
            return
    Hundreds += 1
    n1 = Hundreds*100 + 9
    n2 = Hundreds*100 + 90
    
    if l <= n1 <= u:
        if f(n1) == 9:
            print(n1)
            return
    
    if l <= n2 <= u:
        if f(n2) == 9:
            print(n2)
            return
    
    Hundreds += 1
    n1 = Hundreds*100 + 9
    n2 = Hundreds*100 + 90
    n1 = Hundreds*100 + 9
    n2 = Hundreds*100 + 90
    
    if l <= n1 <= u:
        if f(n1) == 9:
            print(n1)
            return
    
    if l <= n2 <= u:
        if f(n2) == 9:
            print(n2)
            return


    m = -1
    max_n = -1
    for n in range(l, u+1):
        if f(n) > m:
            m = f(n)
            max_n = n
    print(max_n)

for _ in range(int(input())):
    solve()