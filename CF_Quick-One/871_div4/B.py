from sys import stdin
def input(): return stdin.readline()[:-1]

string = 'codeforces'

k = int(input())
for i in range(k):
    N = int(input())
    arr = list(map(int, input().split()))

    string = ''.join(map(str, arr))
    string = string.split('1')
    print(max(map(len, string)))