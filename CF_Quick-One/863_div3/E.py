from sys import stdin
def input(): return stdin.readline()[:-1]


def oi():
    return int(input())


def ti():
    return map(int, input().split())


def mi():
    return list(map(int, input().split()))


arr = ['0', '1', '2', '3', '5', '6', '7', '8', '9']


def solve():
    k = int(input())
    ans = ''
    while k > 0:
        dig = k % 9
        k //= 9
        ans += arr[dig]
    print(ans[::-1])


for _ in range(oi()):
    solve()
