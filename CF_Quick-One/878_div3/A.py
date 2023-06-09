from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N = int(input())
    string = input().strip()
    ans = []
    ON = False
    prev = None
    for i in string:
        if ON == False:
            ans.append(i)
            ON = True
            prev = i
        elif ON == True and prev == i:
            ON = False
            prev = None
    print(''.join(ans))


for _ in range(int(input())):
    solve()