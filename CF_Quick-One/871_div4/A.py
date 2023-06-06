from sys import stdin
def input(): return stdin.readline()[:-1]

string = 'codeforces'

k = int(input())
for i in range(k):
    s = input().strip()
    ans = 0
    for a,b in zip(string,s):
        if a == b:
            ans += 1
    print(10 - ans)