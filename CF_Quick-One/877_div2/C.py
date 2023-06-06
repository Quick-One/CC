from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N, M = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    if N >= 5:
        indexes = []
        indexes.extend(range(0, N, 2))
        indexes.extend(range(1, N, 2))

        for i in range(N):
            for j in range(M):
                arr[i][j] = i * M + j + 1
        final_arr = [0] * N
        for i in range(N):
            final_arr[i] = arr[indexes[i]]
    else:
        s = 1
        for j in range(M):
            for i in range(N):
                arr[i][j] = s
                s += 1
        final_arr = arr
    for row in final_arr:
        print(*row)

    

for _ in range(int(input())):
    solve()