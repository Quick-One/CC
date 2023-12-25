from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    if (int(input()) % 3 == 0):
        print("Second")
    else:
        print("First")

for _ in range(int(input())):
    solve()