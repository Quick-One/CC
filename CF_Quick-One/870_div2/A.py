from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    visited = set()

    for index, val in enumerate(arr):
        if val in visited:
            continue
        visited.add(val)

        lower = val

        upper = float('inf')
        if index != 0:
            upper = arr[index - 1]
        
        honest = N - index
        liars = N - honest

        if lower <= liars < upper:
            print(liars)
            return

    print(-1)

for _ in range(int(input())):
    solve() 