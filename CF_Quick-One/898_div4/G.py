from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    s = input()
    k = set(s)

    if len(k) == 1:
        print(0)
        return
    
    cnt = s.count('A')
    if (s[0] == 'B') or (s[-1] == 'B') or ('BB' in s):
        print(cnt)
        return
    
    groups = []
    temp = []
    for i in s:
        if i == 'A':
            temp.append(i)
        else:
            groups.append(temp)
            temp = []
    if temp:
        groups.append(temp)
    groups = [len(i) for i in groups]
    groups.sort()
    print(sum(groups) - groups[0])

for _ in range(int(input())):
    solve()