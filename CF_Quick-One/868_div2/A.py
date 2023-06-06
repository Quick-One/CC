from sys import stdin
def input(): return stdin.readline()[:-1]
 
def solve():
    N, K = map(int, input().split())
    arr = [0] * (N+1)

    for i in range(N+1):
        a = i
        b = N - i

        arr[i] += a * (a-1) // 2
        arr[i] += b * (b-1) // 2
        if arr[i] == K:
            print("YES")
            e = [1] * a + [-1] * b
            print(*e)
            return
        
    print("NO")




for _ in range(int(input())):
    solve()