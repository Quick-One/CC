from sys import stdin
def input(): return stdin.readline()[:-1]

from collections import deque, defaultdict

def checker(n, end, intervals, queries):
    arr = [0] * n
    
    for i in queries[ : end + 1]:
        arr[i] = 1

    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + arr[i - 1]
    
    for a, b in intervals:
        elements = b - a + 1
        ones_required = elements // 2 + 1
        if prefix_sum[b + 1] - prefix_sum[a]>= ones_required:
            return True
    return False
        

def solve():
    n, m = map(int, input().split())
    intervals = []
    for _ in range(m):
        a,b=  map(int, input().split())
        a -= 1
        b -= 1
        intervals.append((a,b))
    
    q = int(input())
    queries = [ int(input()) for _ in range(q)]
    queries = [i - 1 for i in queries]

    start = 0
    end = q - 1

    while start < end:
        mid = (start + end) // 2
        if checker(n, mid, intervals, queries):
            end = mid
        else:
            start = mid + 1
    if checker(n, start, intervals, queries):
        print(start+1)
    else:
        print(-1)
    

for _ in range(int(input())):
    solve()