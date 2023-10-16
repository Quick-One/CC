from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N = int(input())
    # list of odd numbers of size N starting from 1

    A = [2*i + 1 for i in range(N)]
    print(*A)

for _ in range(int(input())):
    solve() 