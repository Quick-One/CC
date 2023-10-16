from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    string = 'abc'
    s= input()
    k = 0
    for a, b in zip(s, string):
        k += (a == b)
    if k in [3, 1]:
        print("YES")
    else:
        print("NO")

for _ in range(int(input())):
    solve()