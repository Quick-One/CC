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

    if size <= k:
        if s1 == s2:
            print('Yes')
        else:
            print('No')
        return
    
    if size >= 2*k:
        if check (s1, s2):
            print('Yes')
        else:
            print('No')
        return
    
    alpha = size - k
    a_start = s1[:alpha]
    a_end = s1[-alpha:]
    b_start = s2[:alpha]
    b_end = s2[-alpha:]
    a_midddle = s1[alpha:-alpha]
    b_middle = s2[alpha:-alpha]

    if check(a_start+a_end, b_start+b_end) and a_midddle == b_middle:
        print('Yes')
    else:
        print('No')
    

    
for _ in range(oi()):
    solve()