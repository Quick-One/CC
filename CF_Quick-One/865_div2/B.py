from sys import stdin
def input(): return stdin.readline()[:-1]

def oi():
    return int(input())
 
def ti():
    return map(int, input().split())
 
def mi():
    return list(map(int, input().split()))
 
def solve():
    n = oi()
    # make array of 2 x n   
    A = [[0]*n for _ in range(2)]
    arr= list(range(n+1, 2*n+1))
    arr.reverse()
    arr2 = [0] * n

    for i in range(n):
        if i % 2 == 0:
            k = i //2
            arr2[k] = arr[i]
        else:
            k = i //2
            arr2[-k-1] = arr[i]
    # print(*arr2)

    arr3 = list(range(1, n+1))
    arr3.reverse()
    arr4 = [0] * n

    for i in range(n):
        if i % 2 == 0:
            k = i //2
            arr4[k] = arr3[i]
        else:
            k = i //2
            arr4[-k-1] = arr3[i]
    # print(*arr4)

    for i in range(n):
        if i % 2 == 0:
            A[0][i] = arr2[i]
            A[1][i] = arr4[i]
        else:
            A[0][i] = arr4[i]
            A[1][i] = arr2[i]

    for i in range(2):
        print(*A[i])


    
for _ in range(oi()):
    solve()