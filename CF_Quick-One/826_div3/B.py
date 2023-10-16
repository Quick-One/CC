from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N = int(input())
    if N == 3:
        print(-1)
        return

    if N % 2 == 0:
        arr = [i+1 for i in range(0, N)]
        print(*arr[::-1])
        return

    middle = (N+1)//2
    arr = [i+1 for i in range(0, N)]
    arr= arr[::-1]
    arr[middle-1:] = arr[middle-1:][::-1]
    print(*arr)

for _ in range(int(input())):
    solve()