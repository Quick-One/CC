from sys import stdin
def input(): return stdin.readline()[:-1]

from math import isqrt

def solve():
    s1 = input().strip()
    s2 = input().strip()
    s3 = input().strip()
    
    for s in [s1, s2, s3]:
        if '?' in s:
            aloha = s
            if 'A' not in aloha:
                print('A')
            elif 'B' not in aloha:
                print('B')
            else:
                print('C')
    

for _ in range(int(input())):
    solve()