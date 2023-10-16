from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N = int(input())
    arr = list(map(int, input().split()))
    K = int(input())

    current_mini = arr[-1]
    cost_index = {}
    cost_index[current_mini] = N-1
    for i in range(N-2, -1, -1):
        if arr[i] < current_mini:
            current_mini = arr[i]
            cost_index[current_mini] = i
    
    # print(cost_index)

    keys = sorted(cost_index.keys())
    cost_a = {}
    cost_a[keys[0]] = K//keys[0]

    x = K%keys[0]
    for i in range(1, len(keys)):
        term1 = cost_a[keys[i-1]]
        term2 = x // (keys[i] - keys[i-1])
        cost_a[keys[i]] = min(term1, term2)
        cost_a[keys[i-1]] -= cost_a[keys[i]]
        x -= cost_a[keys[i]] * (keys[i] - keys[i-1])
    
    suffix = [0]*N
    for key in keys:
        suffix[cost_index[key]] = cost_a[key]
    ANS = [0] * N
    ANS[-1] = suffix[-1]

    for i in range(N-2, -1, -1):
        ANS[i] = ANS[i+1] + suffix[i]
    print(*ANS)
    
    


for _ in range(int(input())):
    solve()