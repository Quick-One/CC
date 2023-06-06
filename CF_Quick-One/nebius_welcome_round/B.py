def oi():
    return int(input())
 
def ti():
    return map(int, input().split())
 
def mi():
    return list(map(int, input().split()))

from collections import deque
def solve():
    N, size, lifetime, wait = ti()
    A = deque(map(int, input().split()))


    ans = 0
    while len(A) > 0:
        ans += 1
        inventory = size
        start = A[0] + wait
        end = start + lifetime

        while len(A) > 0 and A[0] <= end and inventory > 0:
            A.popleft()
            inventory -= 1

    print(ans)

for _ in range(oi()):
    solve()