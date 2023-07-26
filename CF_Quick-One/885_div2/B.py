from sys import stdin
def input(): return stdin.readline()[:-1]



def compute(arr):
    a = []
    for i in range(len(arr)-1):
        a.append(arr[i+1] - arr[i] - 1)
    a = sorted(a)
    return (max(a[-1]//2, a[-2]))

def solve():
    N, K = map(int, input().split())
    colors = list(map(int, input().split()))

    d = {}
    for i, val in enumerate(colors):
        if val not in d:
            d[val] = [0]
        d[val].append(i+1)
    for k in d:
        d[k].append(N+1)
    # print(d)
    ans = float('inf')
    for k, v in d.items():
        # print(k, v, compute(v))
        ans = min(ans, compute(v))
    
    print(ans)
    

for _ in range(int(input())):
    solve()