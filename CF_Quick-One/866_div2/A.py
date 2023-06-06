def solve():
    s =  input().strip()
    s = s.replace('_','0')
    s = s.replace('^','1')
    if '0' not in s:
        N = len(s)
        if N == 1:
            print(1)
        else:
            print(0)
    elif '1' not in s:
        N = len(s)
        print(N-1+2)
    else:
        splitted = s.split('1')
        a = list(map(len, splitted))
        # print(a)
        ans = 0
        ans += a[0]
        ans += a[-1]
        for i in a[1:-1]:
            if i != 0:
                ans += i -1
        print(ans)
 
t = int(input())
for _ in range(t):
    solve()