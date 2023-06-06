from sys import stdin
def input(): return stdin.readline()[:-1]
 
 
from string import ascii_lowercase as alp
 
def e(n):
    if n == 0:
        return 0
 
    return len(bin(n)[2:])
 
# alp = 'a'
def solve():
    string = input().strip()
    s=set(string)
 
    ans = float('inf')
    for char in alp:
        if char not in s:
            continue
        ind = []
        for i in range(len(string)):
            if string[i] == char:
                ind.append(i)
        arr2 = []
        for i in range(len(ind)-1):
            arr2.append(ind[i+1]-ind[i] - 1)
        arr2.append(ind[0] - 0)
        arr2.append(len(string) - ind[-1] -1)
        # print(arr2)
        k = max(arr2)
        # print(k)
        ans = min(e(k), ans)
    print(ans)
 
for _ in range(int(input())):
    solve()