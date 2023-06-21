from sys import stdin
def input(): return stdin.readline()[:-1]


def solve():
    a,b = input().split()
    a = '0' * (len(b) - len(a)) + a

    ans = 0
    for i in range(len(b)):
        if a[i] == b[i]:
            continue
        else:
            ans += int(b[i]) - int(a[i])
            ans += (len(b) - i - 1) * 9
            break
    print(ans)

        
        


for _ in range(int(input())):
    solve()