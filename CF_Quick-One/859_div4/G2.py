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
    arr.sort()

    if N == 1 and arr[0] != 1:
        print("NO")
        return
    if N == 1 and arr[0] == 1:
        print("YES")
        return
    
    s = 1
    # print(arr)
    for i in range(1, N):
        element =  arr[i]
        # print(i, element, s)
        if element > s:
            # print(element, s)
            print("NO")
            return
        s += element
    print("YES")
    
for _ in range(oi()):
    solve()