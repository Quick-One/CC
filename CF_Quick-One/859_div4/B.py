from sys import stdin
def input(): return stdin.readline()[:-1]

def oi():
    return int(input())
 
def ti():
    return map(int, input().split())
 
def mi():
    return list(map(int, input().split()))
 
def solve():
    n = oi()
    a = mi()

    even_sum = 0
    odd_sum = 0
    for i in a:
        if i % 2 == 0:
            even_sum += i
        else:
            odd_sum += i
    
    # print(even_sum, odd_sum)
    if even_sum > odd_sum:
        print("YES")
    else:
        print("NO")
    
for _ in range(oi()):
    solve()