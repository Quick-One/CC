from sys import stdin
def input(): return stdin.readline()[:-1]
 
 
from collections import Counter
def solve():
    string = input().strip()
    N = len(string)
    e = Counter(string)
    f = e['?']
    # print(f, string)
    if f == 0:
        if int(string) == 0:
            print(0)
        elif string[0] == '0':
            print(0)
        else:
            print(1)
        return
    if string[0] == '0':
        print(0)
        return
 
    if string[0] == '?':
        ans = 9 * 10 ** (f - 1)
    else:
        ans = 10 ** f
    print(ans)
 
for _ in range(int(input())):
    solve()