from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N = int(input())
    string = input().strip()
    d= []
    for i in range(N-1):
        s = string[i:i+2]
        d.append(s)
    print(len(set(d)))

for _ in range(int(input())):
    solve()