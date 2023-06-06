from sys import stdin
def input(): return stdin.readline()[:-1]

def oi():
    return int(input())
 
def ti():
    return map(int, input().split())
 
def mi():
    return list(map(int, input().split()))
 
def solve():
    a,b = ti()
    num_string = input().strip()
    index = a
    for i, dig in enumerate(num_string):
        if b > int(dig):
            index = i
            break
    ans = num_string[:index] + str(b) + num_string[index:]
    print(ans)
    
for _ in range(oi()):
    solve()