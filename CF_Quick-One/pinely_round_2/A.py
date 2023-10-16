from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    n, a, q = map(int, input().split())
    s = input().strip()
    if a == n:
        print("YES")
        return
    c = a
    for i in s:
        if i == '-':
            c -= 1
        else:
            c += 1
        if c == n:
            print("YES")
            return

    if a + s.count('+') >= n:
        print("MAYBE")
        return

    print("NO")
        

for _ in range(int(input())):
    solve()
    