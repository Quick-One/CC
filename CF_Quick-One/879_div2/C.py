from sys import stdin
def input(): return stdin.readline()[:-1]

def deformity(s1, s2):
    cnt = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            cnt += 1
    return cnt

def solve():
    N = int(input())
    s1 = input().strip()
    s2 = input().strip()

    # lets say b moves are even
    d1 = deformity(s1, s2)
    if d1 == 0:
        print(0)
        return

    if d1 % 2 == 1:
        a1 = d1 * 2 - 1
    else:
        a1 = d1 * 2
    
    d2 = deformity(s1, s2[::-1])
    if d2 == 0:
        a2 = 2
    else:
        if d2 % 2 == 1:
            a2 = d2 * 2
        else:
            a2 = (d2) * 2 - 1
    # print(a1, a2)
    print(min(a1, a2))
            
        


for _ in range(int(input())):
    solve()