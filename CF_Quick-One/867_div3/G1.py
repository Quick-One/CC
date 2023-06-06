from sys import stdin
def input(): return stdin.readline()[:-1]


from math import sqrt

def solve():
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    d = {}
    for element in arr:
        if element not in d:
            d[element] = 0
        d[element] += 1
    
    ans = 0
    for v in d.values():
        ans += v * (v-1) * (v-2)
    # print(d)
    # print(ans)
    for mul in range(2, int(sqrt(arr[-1]))+2):
        for element in d.keys():
            e1 = element * mul
            e2 = e1 * mul

            if e2 > arr[-1]:
                break

            if e1 in d and e2 in d:
                ans += d[e1] * d[e2] * d[element]
    
    print(ans)


    
for _ in range(int(input())):
    solve()