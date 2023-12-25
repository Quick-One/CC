from sys import stdin
def input(): return stdin.readline()[:-1]

def dig_sum(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

def solve():
    N, K = map(int, input().split())
    
    while dig_sum(N) % K != 0:
        N += 1
    print(N)
            

for _ in range(int(input())):
    solve()