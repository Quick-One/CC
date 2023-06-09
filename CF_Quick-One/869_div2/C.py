from sys import stdin
def input(): return stdin.readline()[:-1]

N, K = map(int, input().split())
arr = list(map(int, input().split()))

from bisect  import bisect_left, bisect_right

from collections import Counter
mapping_arr = [0] * (N)
mapping_arr[0] = 0
for i in range(1, N):
    if arr[i] > arr[i-1]:
        mapping_arr[i] = mapping_arr[i-1] + 1
    else:
        mapping_arr[i] = mapping_arr[i-1]
c = Counter(mapping_arr)
vals = list(Counter(mapping_arr).values())
vals[0] = min(vals[0], 2)
for i in range(1, len(vals)):
    vals[i] = min(vals[i], 2)
    vals[i] += vals[i-1]
# print(mapping_arr)
# print(vals)
for q in range(K):
    l, r = map(int, input().split())
    l -= 1
    r -= 1

    left = mapping_arr[l]
    right = mapping_arr[r]
    if mapping_arr[l] == mapping_arr[r]:
        ans = min(r-l+1, 2)
        print(ans)
    else:
        ans = 0
        # print(left, right)
        ans += min(bisect_right(mapping_arr, left) - l, 2)
        # print(ans)
        ans += min(r - bisect_left(mapping_arr, right) + 1, 2)
        # print(ans)
        ans += vals[right-1] - vals[left]
        print(ans)

        
