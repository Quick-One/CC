from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N = int(input())
    ans = 0
    i = 1
    while True:
        if N % i  == 0:
            ans += 1
        else:
            break
        i += 1
    print(ans)
    

for _ in range(int(input())):
    solve()