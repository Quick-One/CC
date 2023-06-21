from sys import stdin
def input(): return stdin.readline()[:-1]


def solve():
    N = int(input())
    cnt = [0] * 100
    arr = list(map(int, input().split()))

    for i in arr:
        cnt[i] += 1
    
    for i in range(1, 100):
        if cnt[i] > cnt[i-1]:
            print("NO")
            return
    print("YES")



for _ in range(int(input())):
    solve()