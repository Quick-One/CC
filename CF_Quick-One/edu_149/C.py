from sys import stdin
def input(): return stdin.readline()[:-1]
 
def solve():
    string = input()
    N = len(string)
    ans = list(string)
    l = 0
    r = len(string) - 1
    while l < N and ans[l] == '?':
        ans[l] = 0
        l += 1
    
    while r >= 0 and ans[r] == '?':
        ans[r] = 1
        r -= 1
    
    for i in range(N):
        if ans[i] == '?':
            l = i
            r = i
            while ans[r] == '?':
                r += 1
            r -= 1
            for i in range(l , r+1):
                ans[i] = ans[l-1]    
    print(''.join(map(str, ans)))
 
        
 
for _ in range(int(input())):
    solve()