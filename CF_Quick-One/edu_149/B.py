from sys import stdin
def input(): return stdin.readline()[:-1]
 
def solve():
    N = int(input())
    string = input()
    a = []
    prev = string[0]
    l = 1
    for i in range(1, N):
        if string[i] == prev:
            l += 1
        else:
            a.append(l)
            l = 1
            prev = string[i]
    a.append(l)
    print(max(a) + 1)
 
        
 
for _ in range(int(input())):
    solve()