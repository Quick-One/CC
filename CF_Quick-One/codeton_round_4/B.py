def solve():
    N = int(input())
    bin_string = bin(N)[2:]
    s = len(bin_string)

    if s - 1 > 40 or N%2 == 0:
        print(-1)
    else:
        print(s-1)
        ans = bin_string[:-1]
        ans = ans.replace('1', '2')
        ans = ans.replace('0', '1')
        print(' '.join(ans))


for _ in range(int(input())):
    solve()