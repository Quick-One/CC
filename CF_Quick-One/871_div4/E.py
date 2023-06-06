from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    n, m = map(int, input().split())
    visited = set()
    array = []


    for _ in range(n):
        array.append(list(map(int, input().split())))
    ans = 0
    for i in range(n):
        for j in range(m):
            if (i, j) in visited:
                continue
            if array[i][j] == 0:
                continue
            temp = 0
            dfs = []
            visited.add((i, j))
            dfs.append((i, j))
            while dfs:
                x, y = dfs.pop()
                temp += array[x][y]
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited and array[nx][ny] != 0:
                        visited.add((nx, ny))
                        dfs.append((nx, ny))
            ans = max(ans, temp)
    print(ans)

for _ in range(int(input())):
    solve()