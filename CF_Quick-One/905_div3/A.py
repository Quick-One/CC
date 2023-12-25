from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    string = input()
    a =[1]
    for i in string:
        if i == '0':
            a.append(10)
            continue
        a.append(int(i))
    ans = 4
    for i in range(1, 5):
        ans += abs(a[i] - a[i-1])
    print(ans)

for _ in range(int(input())):
    solve()