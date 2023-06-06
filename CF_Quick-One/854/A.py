def oi():
    return int(input())
 
def ti():
    return map(int, input().split())
 
def mi():
    return list(map(int, input().split()))
 
def solve():
    N, M = ti()
    arr = mi()
    ans_arr = [-1] * N

    visited = set()
    pointer = N-1
    for index,i in enumerate(arr, start=1):
        if pointer < 0:
            break
        if i not in visited:
            visited.add(i)
            ans_arr[pointer] = index
            pointer -= 1
    print(*ans_arr)

for _ in range(oi()):
    solve()