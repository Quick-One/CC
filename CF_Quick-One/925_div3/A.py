from sys import stdin
def input(): return stdin.readline()[:-1]

from string import ascii_lowercase

def solve():
    n = int(input())
    n -= 3
    
    ans = []
    while n > 25:
        n -= 25
        ans.append(25)
    ans.append(n)
    ans  = ans + [0] * (3 - len(ans))
    ans.reverse()
    
    s = []
    for i in ans:
        s.append(ascii_lowercase[i])
    print(''.join(s))
        
        

for _ in range(int(input())):
    solve()