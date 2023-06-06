def oi():
    return int(input())

def ti():
    return map(int, input().split())

def mi():
    return list(map(int, input().split()))

def solve():
    s = input()
    string = input().strip()
    while True:
        if len(string) == 0:
            break
        
        s = string[0]
        e = string[-1]
        if s == e:
            break
        string = string[1:-1]
    print(len(string))
    
for _ in range(oi()):
    solve()