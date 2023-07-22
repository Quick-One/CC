from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    s = []
    for _ in range(8):
        s.append(input().strip())
    s = ''.join(s)
    s = s.replace('.','')
    print(s)
        
for _ in range(int(input())):
    solve() 