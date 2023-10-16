from sys import stdin
def input(): return stdin.readline()[:-1]

def prod(arr):
    mul = 1
    for i in arr:
        mul *= i
    return mul

def solve():
    N = int(input())
    A = list(map(int, input().split()))

    count1 = 0
    for i in A:
        if i != 1:
            count1 += 1
    
    if count1 > 18:
        # get the left most and right most non 1

        left = -1
        right = -1
        for i in range(N):
            if A[i] != 1:
                left = i
                break
        for i in range(N-1, -1, -1):
            if A[i] != 1:
                right = i
                break
        print(left + 1, right + 1)
        return

    # get groups of non 1s together along with their indices
    groups = []
    temp = []
    for i in range(N):
        if A[i] != 1:
            temp.append(i)
        else:
            if len(temp) > 0:
                groups.append(temp)
                temp = []
    
    if len(temp) > 0:
        groups.append(temp)

    if len(groups) == 0:
        print(1,1)
        return
    
    best = 0
    best_left = 0
    best_right = 0
    prefix_sum = [0] * (N+1)
    for i in range(N):
        prefix_sum[i+1] = prefix_sum[i] + A[i]
    

    # print(groups)
    for i in range(len(groups)):
        starting_group = groups[i]

        product = prod([A[i] for i in starting_group])
        left = starting_group[0]
        right = starting_group[-1]
        quantity = product - (prefix_sum[right+1] - prefix_sum[left])
        # print(starting_group, quantity)
        if quantity > best:
            best = quantity
            best_left = left
            best_right = right
        
        for j in range(i+1, len(groups)):
            ending_group = groups[j]

            product *= prod([A[i] for i in  ending_group])
            left = starting_group[0]
            right = ending_group[-1]
            quantity = product - (prefix_sum[right+1] - prefix_sum[left])

            if quantity > best:
                best = quantity
                best_left = left
                best_right = right
                # print(starting_group, ending_group, quantity)
    print(best_left + 1, best_right + 1)







for _ in range(int(input())):
    solve()