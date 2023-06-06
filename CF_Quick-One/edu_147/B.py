from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N = int(input())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    index = []
    changed = [False] * N
    for i in range(N):
        if arr1[i] != arr2[i]:
            changed[i] = True
            index.append(i)

    if len(index) == 0:
        # find the longest sorted part in arr1
        pairs = []
        s = 0

        for i in range(1, N):
            if arr1[i] >= arr1[i-1]:
                continue
            else:
                pairs.append((s, i-1))
                s = i
        pairs.append((s, N-1))

        M, ans = 0, 0
        for s, e in pairs:
            delta = e - s + 1
            if delta > M:
                M = delta
                ans = (s, e)
        print(ans[0]+1, ans[1]+1)
        return
            

    l,r = min(index), max(index)

    maxi = arr2[r]
    for i in range(r+1, N):
        if arr2[i] >= maxi:
            maxi = arr2[i]
            r = i
        else:
            break

    mini = arr2[l]
    for i in range(l-1, -1, -1):
        if arr2[i] <= mini:
            mini = arr2[i]
            l = i
        else:
            break
    
    print(l+1, r+1)

for _ in range(int(input())):
    solve()