from math import gcd
def one_input():
    return int(input())

def two_input():
    return map(int, input().split())

def many_input():
    return list(map(int, input().split()))

def solve():
    n = one_input()
    arr = many_input()

    s  = sum(arr)
    prefix_sum = [0]
    for i in range(n):
        prefix_sum.append(prefix_sum[-1] + arr[i])
    l = []
    prefix_sum = prefix_sum[1:-1]
    for i in prefix_sum:
        l.append(gcd(i, s-i))
    print(max(l))
    


for _ in range(one_input()):
    solve()