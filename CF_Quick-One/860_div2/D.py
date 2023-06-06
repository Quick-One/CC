from sys import stdin
def input(): return stdin.readline()[:-1]

def oi():
    return int(input())
 
def ti():
    return map(int, input().split())
 
def mi():
    return list(map(int, input().split()))
 
def solve():
    N = oi()
    arr = mi()
    Q = max(arr) - min(arr)

    if len(set(arr)) == 1:
        print("NO")
        return


    positive = []
    negative = []
    zero = 0
    for i in range(N):
        if arr[i] == 0:
            zero += 1
        elif arr[i] > 0:
            positive.append(arr[i])
        else:
            negative.append(arr[i])
    positive.sort()
    negative.sort(reverse=True)

    # print(positive)
    # print(negative)

    print("YES")
    ans = []
    for i in range(zero):
        ans.append(0)
    s = positive[-1]
    ans.append(positive[-1])
    positive.pop()
    while True:
        if len(positive) == 0 and len(negative) == 0:
            break
        if s > 0:
            s += negative[-1]
            ans.append(negative[-1])
            negative.pop()
        else:
            s += positive[-1]
            ans.append(positive[-1])
            positive.pop()
    print(*ans)
    

    
for _ in range(oi()):
    
    # print("Case #{}:".format(_+1), end=" ")
    solve()