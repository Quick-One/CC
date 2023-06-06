from sys import stdin
def input(): return stdin.readline()[:-1]

def oi():
    return int(input())
 
def ti():
    return map(int, input().split())
 
def mi():
    return list(map(int, input().split()))
 
def solve():
    n, s1, s2 = ti()
    a = mi()
    b = list(zip(a, range(1,n+1)))
    b.sort(reverse=True)

    p1 = []
    q1 = 1
    p2 = []
    q2 = 1

    for val, index in b:
        c1 = q1 * val * s1
        c2 = q2 * val * s2

        if c1 < c2:
            p1.append(index)
            q1 += 1
        else:
            p2.append(index)
            q2 += 1
    
    print(len(p1), *p1)
    print(len(p2), *p2)




            
for _ in range(oi()):
    solve()