from sys import stdin
def input(): return stdin.readline()[:-1]

N = int(input())
a = list(map(int, input().split()))
print(min(map(abs, a)))