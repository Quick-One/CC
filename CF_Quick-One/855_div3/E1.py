def oi():
    return int(input())
 
def ti():
    return map(int, input().split())
 
def mi():
    return list(map(int, input().split()))

def check(s1, s2):
    count_s1 = [0]*26
    count_s2 = [0]*26
    
    for i in range(len(s1)):
        count_s1[ord(s1[i])-ord('a')] += 1
        count_s2[ord(s2[i])-ord('a')] += 1
    
    for i in range(26):
        if count_s1[i] != count_s2[i]:
            return False
    return True


def solve():
    size, k  = ti()
    s1 = input().strip()
    s2 = input().strip()

    if not check(s1,s2):
        print('No')
        return

    if size in [1,2,3]:
        if s1 == s2:
            print('Yes')
        else:
            print('No')
        return

    if size == 4:
        a = s1[0] + s1[-1]
        b = s2[0] + s2[-1]
        if check(a,b) and s1[1] == s2[1] and s1[2] == s2[2]:
            print('Yes')
        else:
            print('No')
        return

    if size == 5:
        a = s1[0] + s1[1] + s1[-1] + s1[-2]
        b = s2[0] + s2[1] + s2[-1] + s2[-2]
        if check(a,b) and s1[2] == s2[2]:
            print('Yes')
        else:
            print('No')
        return

    else:
        if check(s1,s2):
            print('Yes')
        else:
            print('No')
        return
    

    
for _ in range(oi()):
    solve()