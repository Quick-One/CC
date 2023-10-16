from sys import stdin
def input(): return stdin.readline()[:-1]


def solve():
    N, K = map(int, input().split())
    string = input().strip()
    l = list(map(int, input().split()))
    r = list(map(int, input().split()))
    l = [i-1 for i in l]    
    r = [i-1 for i in r]

    
    temp = [0] * N
    cnt = 0
    for x,y in zip(l, r):
        for i in range(x, y+1):
            temp[i] = cnt
        cnt += 1

    Q = int(input())
    queries = list(map(int, input().split()))
    queries = [i-1 for i in queries]
    
    prefix = [0] * (N+1)
    for q in queries:
        index = temp[q]
        l1, r1 = l[index], r[index]
        a = min(q, l1 + r1 - q)
        b = max(q, l1 + r1 - q)

        prefix[a] += 1
        prefix[b+1] -= 1
    
    for i in range(1, N+1):
        prefix[i] += prefix[i-1]
    
    # print(*prefix)

    ans = []
    for i in range(N):
        if prefix[i] % 2 == 0:
            ans.append(string[i])
        else:
            index = temp[i]
            l1, r1 = l[index], r[index]
            # print(i, l1 + r1 - i, index)
            ans.append(string[l1 + r1 - i])
    ANS = ''.join(ans)
    print(ANS)

    
    


for _ in range(int(input())):
    solve() 