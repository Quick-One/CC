def oi():
    return int(input())
 
def ti():
    return map(int, input().split())
 
def mi():
    return list(map(int, input().split()))
 
def solve():
    length, c = ti()
    arr = mi()
    for i, num in enumerate(arr):
        arr[i] = num + i + 1
    arr.sort()

    ans = 0
    p = 0
    while c > 0:
        if len(arr) == p:
            break
        if c >= arr[p]:
            c -= arr[p]
            ans += 1
            p += 1
        else:
            break
    print(ans)
    
for _ in range(oi()):
    solve()