from sys import stdin
def input(): return stdin.readline()[:-1]

limit = 10 ** 6
squares = [n * n for n in range(limit+1)]
dp = [0] * (limit+1)

from collections import defaultdict
d = defaultdict(list)


end = 0
r = 1
while end <= limit:
    end = r * (r+1) // 2
    start = end - r + 1

    for elem in range(start, end+1):
        d[elem + r].append(elem)
        d[elem + r+1].append(elem)
    
    r += 1


def solve(N):
    parents = d[N]
    if len(parents) == 0:
        return 1
    elif len(parents) == 1:
        return (squares[N] + dp[parents[0]])
    else:
        e1, e2 = parents
        par_e1 = d[e1]
        par_e2 = d[e2]
        # intersection of par_e1 and par_e2
        common = set(par_e1) & set(par_e2)
        common = list(common)[0]

        ans = squares[N] + dp[e1] + dp[e2] - dp[common]
        return ans
    

for i in range(1, limit+1):
    dp[i] = solve(i)

for _ in range(int(input())):
    N = int(input())
    print(dp[N])