from sys import stdin
def input(): return stdin.readline()[:-1]

def countey(array):
    d = {}
    prev = array[0]
    cnt = 1
    for i in range(1, len(array)):
        if prev == array[i]:
            cnt += 1
        else:
            if prev in d:
                d[prev] = max(d[prev], cnt)
            else:
                d[prev] = cnt
            prev = array[i]
            cnt = 1
    
    if prev in d:
        d[prev] = max(d[prev], cnt)
    else:
        d[prev] = cnt
    
    return d
    

def solve():
    N = int(input())
    A1 = list(map(int, input().split()))
    A2 = list(map(int, input().split()))
    c1 = countey(A1)
    c2 = countey(A2)

    ans = -1
    for k in c1:
        if k in c2:
            ans = max(ans, c1[k] + c2[k])
        else:
            ans = max(ans, c1[k])

    for k in c2:
        if k in c1:
            ans = max(ans, c1[k] + c2[k])
        else:
            ans = max(ans, c2[k])
    
    print(ans)




for _ in range(int(input())):
    solve()