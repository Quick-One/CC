from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    string_num = input().strip()
    s = list(map(int, string_num))
    s.insert(0, 0)
    max_index = -1
    for index in range(len(s)-2, -1, -1 ):
        if s[index+1] >= 5:
            s[index] += 1
            s[index+1] = 0
            max_index = index

            while s[index] >= 10:
                s[index] -= 10
                s[index-1] += 1
                index -= 1
    
    if max_index != -1:
        for i in range(max_index+1, len(s)):
            s[i] = 0

    if s[0] == 0:
        s.pop(0)
    
    print(''.join(map(str, s)))





for _ in range(int(input())):
    solve()