from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    s1 = []
    s2 = []

    string = input().strip()

    for i, char in enumerate(string):
        if char == 'b':
            if s1: s1.pop()
        elif char == 'B':
            if s2: s2.pop()
        elif char.isupper():
            s2.append(i)
        else:
            s1.append(i)
    
    ANS = [string[i] for i in sorted(s1 + s2)]
    print(''.join(ANS))

for _ in range(int(input())):
    solve()