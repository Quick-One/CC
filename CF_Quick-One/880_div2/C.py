from sys import stdin
def input(): return stdin.readline()[:-1]


def solve():
    A, B, C, K = map(int, input().split())
    K -= 1
    A_lower = 10**(A-1)
    A_higher = 10**A - 1
    for a in range(A_lower, A_higher+1):
        b_lower = max(10**(C-1) - a, 10**(B-1))
        b_higher = min(10**C - 1 - a, 10**B - 1)
        interval = b_higher - b_lower + 1
        if interval <= 0:
            continue
        if K < interval:
            final_b = b_lower + K
            final_c = final_b + a
            print(f'{a} + {final_b} = {final_c}')
            return
        else:
            K -= interval
    print(-1)
        
        


for _ in range(int(input())):
    solve()