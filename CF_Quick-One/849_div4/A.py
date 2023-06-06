def oi():
    return int(input())

def ti():
    return map(int, input().split())

def mi():
    return list(map(int, input().split()))

def solve():
    char = input().strip()
    if char in "codeforces":
        print("YES")
    else:
        print("NO")
    
for _ in range(oi()):
    solve()