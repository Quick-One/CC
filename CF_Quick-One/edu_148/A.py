from sys import stdin
def input(): return stdin.readline()[:-1]

from collections import Counter
def solve():
    s = input().strip()
    c = Counter(s)


    mid = s[ : (len(s) ) // 2]
    if len(Counter(mid)) == 1:
        print("NO")
    else:
        print("YES")
for _ in range(int(input())):
    solve()