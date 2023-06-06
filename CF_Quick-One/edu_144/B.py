def oi():
    return int(input())
 
def ti():
    return map(int, input().split())
 
def mi():
    return list(map(int, input().split()))

def pairs(s):
    for i in range(len(s)-1):
        yield s[i:i+2]

def solve():
    s1 = input().strip()
    s2 = input().strip()

    if s1[0] == s2[0]:
        print("YES")
        print(f"{s1[0]}*")
        return

    if s1[-1] == s2[-1]:
        print("YES")
        print(f"*{s1[-1]}")
        return
    
    if len(s1) == 1:
        print("NO")
        return
    
    for p1 in pairs(s1):
        if p1 in s2:
            print("YES")
            print(f"*{p1}*")
            return
    print("NO")
    return


     

    
for _ in range(oi()):
    solve()