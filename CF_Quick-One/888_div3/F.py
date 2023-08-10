from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    groups = [A]
    for k in range(K-1, -1, -1):
        mask = 1 << k
        new_groups = []
        for grup in groups:
            grup_0 = []
            grup_1 = []
            for a in grup:
                if a & mask:
                    grup_1.append(a)
                else:
                    grup_0.append(a)
            if grup_0:
                new_groups.append(grup_0)
            if grup_1:
                new_groups.append(grup_1)
        something = max(len(grup) for grup in new_groups)
        if something == 1:
            continue
        else:
            groups = []
            for grup in new_groups:
                if len(grup) > 1:
                    groups.append(grup)
    
    ans = float('-inf')
    pair = None
    for p in groups:
        if len(p) == 2:
            val = (2<<K) - 1
            val -= (p[0] ^ p[1])
            if val > ans:
                ans = val
                pair = p
        else:
            val = (1<<K) - 1
            val -= (p[0] ^ p[1])
            if val > ans:
                ans = val
                pair = (p[0], p[1])
    a,b = pair
    index_a = A.index(a)
    # find inex_b from right
    index_b = N - 1 - A[::-1].index(b)
    index_a += 1
    index_b += 1
    # print(a,b, a|b)
    XOR = ((1<<K)-1) - (a|b)
    print(index_a, index_b, XOR)





for _ in range(int(input())):
    solve()