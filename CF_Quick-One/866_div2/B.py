def solve():
    s = input().strip()
    # print(s)
    if '0' not in s:
        N = len(s)
        print(N*N)
    else:
        splitted = s.split('0')
        a = list(map(len, splitted))
        if s[0] == s[-1] == '1':
            if len(a[1:-1]) == 0:
                a = a[0] + a[-1]
            else:
                b = max(a[1:-1])
                a = max(a[0] + a[-1], b) 
        else:
            a = max(a)
        b = a
        a += 1
        a //=  2
        ans = (b+1-a) * a
        print(ans)
 
t = int(input())
for _ in range(t):
    solve()