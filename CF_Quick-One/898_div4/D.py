from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N , K = map(int,input().split())
    string = input()
    done = -1
    ans = 0


    for i in range(N):
        if string[i] == 'W':
            continue
        if i <= done:
            continue
        ans += 1
        done = i + K - 1

    print(ans)

for _ in range(int(input())):
    solve()