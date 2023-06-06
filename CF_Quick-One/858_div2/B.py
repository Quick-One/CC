from sys import stdin
def input(): return stdin.readline()[:-1]

def oi():
    return int(input())
 
def ti():
    return map(int, input().split())
 
def mi():
    return list(map(int, input().split()))


from collections import Counter
def solve():
    N = oi()
    arr = mi()
    zero_c = 0
    one_c = 0
    non_c = 0

    for i in arr:
        if i == 0:
            zero_c += 1
        elif i == 1:
            one_c += 1
        else:
            non_c += 1
    
    if (N - zero_c) >= zero_c - 1:
        return 0
    
    if (non_c > 0) or (one_c == 0):
        return 1
    
    return 2



for _ in range(oi()):
    print(solve())