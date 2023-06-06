def oi():
    return int(input())
 
def ti():
    return map(int, input().split())
 
def mi():
    return list(map(int, input().split()))

from bisect import bisect_right as br
MAX_NUM = 10**9 + 2
def ceildiv(a, b):
    return -(a // -b)

class Node:
    def __init__(self, val, index):
        self.val = val
        self.index = index
    
    #making the class comparable
    def __lt__(self, other):
        return self.val < other.val
    
    def __repr__(self) -> str:
        return str(self.val)
    

def solve():
    n = oi()
    arr = mi()

    if len(set(arr)) == 1:
        print(0)
        return

    if 1 in arr:
        print(-1)
        return
    
    arr = [Node(i, index) for index, i in enumerate(arr, start=1)]
    arr.sort()
    ans = []

    while arr[0].val != arr[-1].val:
        first_val = arr[0].val
        first_index = arr[0].index

        to_reduce = br(arr, Node(first_val, MAX_NUM))
        elemnt_to_reduce = arr[to_reduce]

        while elemnt_to_reduce.val > first_val:
            elemnt_to_reduce.val = ceildiv(elemnt_to_reduce.val, first_val)
            ans.append((elemnt_to_reduce.index, first_index))
    
        if elemnt_to_reduce.val == first_val:
            continue

        arr[0], arr[to_reduce] = arr[to_reduce], arr[0]
    
    print(len(ans))
    for i in ans:
        print(*i)


    
for _ in range(oi()):
    solve()