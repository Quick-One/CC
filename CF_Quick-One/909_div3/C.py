from sys import stdin
def input(): return stdin.readline()[:-1]

 
 
def maxSubArraySum(a):
    size = len(a)
    max_so_far = float('-inf')
    max_ending_here = 0
 
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
 
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far


def solve():
    N = int(input())
    A = list(map(int, input().split()))

    wow = []
    temp = []
    for i in A:
        if len(temp) == 0:
            temp.append(i)
        else:
            if temp[-1]&1 != i&1:
                temp.append(i)
            else:
                wow.append(temp)
                temp = [i]
    
    if len(temp) > 0:
        wow.append(temp)

    ans = maxSubArraySum(wow[0])
    for i in range(1, len(wow)):
        ans = max(ans, maxSubArraySum(wow[i]))
    print(ans)
            


for _ in range(int(input())):
    solve()