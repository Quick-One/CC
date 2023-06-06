from sys import stdin
def input(): return stdin.readline()[:-1]

def oi():
    return int(input())
 
def ti():
    return map(int, input().split())
 
def mi():
    return list(map(int, input().split()))
 
def solve():
    n = int(input())
    string = input().strip()

    s1 = set(string[0::2])
    s2 = set(string[1::2])

    if len(s1.intersection(s2)) == 0:
        print("YES")
    else:
        print("NO")
    
for _ in range(oi()):
    solve()