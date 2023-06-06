def oi():
    return int(input())

def ti():
    return map(int, input().split())

def mi():
    return list(map(int, input().split()))

def solve():
    size = oi()
    string = input()
    x,y = 0,0
    for char in string:
        if char == 'L':
            x -= 1
        elif char == 'R':
            x += 1
        elif char == 'U':
            y += 1
        else:
            y -= 1
        if x == 1 and y == 1:
            print('YES')
            return
    print('NO')
    
for _ in range(oi()):
    solve()