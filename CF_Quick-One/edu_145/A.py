from sys import stdin
def input(): return stdin.readline()[:-1]

def oi():
    return int(input())
 
def ti():
    return map(int, input().split())
 
def mi():
    return list(map(int, input().split()))

from collections import Counter
def solve():
    string = input().strip()
    c = Counter(string)
    vals = list(c.values())
    vals.sort()

    if len(vals) == 1:
        return -1
    
    if len(vals) == 2 and vals[-1] == 3:
        return 6
    
    else:
        return 4
    

    

    
for _ in range(oi()):
    print(solve())