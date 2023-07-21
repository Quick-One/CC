from sys import stdin
def input(): return stdin.readline()[:-1]

def get_penalty(times, hours, index):
    times.sort()
    prefix_sum = [0] * (len(times) + 1)

    for i in range(len(times)):
        prefix_sum[i+1] = prefix_sum[i] + times[i]
    
    solved = 0
    for i in range(len(prefix_sum)):
        if prefix_sum[i] <= hours:
            solved = i
        else:
            break
    
    score = solved
    penalty = sum(prefix_sum[:solved+1])
    penalty *= -1
    return (score , penalty, -index)

def solve():
    N, M, H  = map(int, input().split())

    A = []
    for i in range(N):
        times = list(map(int, input().split()))
        A.append(get_penalty(times, H, i+1))
    # print(A)
    A.sort(reverse=True)

    for i in range(len(A)):
        if A[i][2] == -1:
            print(i + 1)
            return

for _ in range(int(input())):
    solve()