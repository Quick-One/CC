from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    s = input().strip()
    i3 = s.find('3')
    i7 = s.find('7')
    if i3 < i7:
        print(37)
    else:
        print(73)    
    
t=int(input())  
for _ in range(t):
    solve()