from sys import stdin
def input(): return stdin.readline()[:-1]


def solve():
    N = int(input())
    string = input().strip()
    
    l,r = 0,N-1
    ones = 0
    twos = 0
    extra_one = False

    while l < r:
        left, right = string[l], string[r]
        if left == right:
            twos += 1
        else:
            ones += 1
        l += 1
        r -= 1
    
    if (N%2 == 1):
        extra_one = True

    ANS = [False] * (N+1)
    for i in range(ones, ones + 2 * twos + 1, 2):
        ANS[i] = True
    if extra_one:
        for i in range(N, 0, -1):
            if ANS[i-1]:
                ANS[i] = True
    
    ans_string = []
    for i in ANS:
        if i:
            ans_string.append('1')
        else:
            ans_string.append('0')
    print(''.join(ans_string))


for _ in range(int(input())):
    solve()