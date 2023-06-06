from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N = int(input())
    long = (N* (N+1)) // 2
    short = long - N
    # print(long)
    # print(short)
    l1 = long * 2 + 2
    l2 = short * 2 + 2
    # print(l1, l2)
    size = 4 * N
    intersection = l1 + l2 - size
    intersection = intersection // 2
    ans = size + intersection
    print(ans)

for _ in range(int(input())):
    solve()