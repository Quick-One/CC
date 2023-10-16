from sys import stdin
def input(): return stdin.readline()[:-1]

def ask(a):
    print(a , flush=True)

def MEX(s):
    i = 0
    while True:
        if i not in s:
            return i
        i += 1

def solve():
    N = int(input())
    s = set(map(int, input().split()))
    ask(MEX(s))
    while True:
        response = int(input())
        if response == -1:
            return
        elif response == -2:
            exit()
        ask(response)

for _ in range(int(input())):
    solve()