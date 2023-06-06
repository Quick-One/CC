def oi():
    return int(input())
 
def ti():
    return map(int, input().split())
 
def mi():
    return list(map(int, input().split()))

from collections import Counter
def solve():
    s = input().strip()
    if len(s) == 1:
        print(s)
        return
    if len(set(s)) == 1:
        print(s)
        return
    s = sorted(s, reverse=True)
    ans_string = ""
    
    condition = True
    n = 0
    # pointer = 0
    while condition:
        if len(s) >=2:
            char1,char2 = s[-1], s[-2]
            if char1 == char2:
                ans_string += char1
                s.pop()
                s.pop()
            else:
                if len(s) == 2:
                    a,b = s[0], s[1]
                    a, b= max(a,b), min(a,b)
                    string = ans_string + a + b + ans_string[::-1]
                    print(string)
                    return
                k = set(s[:-2])
                smaller = s[-1]
                larger = s[-2]

                if len(k) == 1 and larger in k:
                    ans_string += larger
                    s.pop(-2)
                    s.pop(-2)

                else:
                    substring = s[:-2][::-1]
                    substring = "".join(substring)
                    substring = larger + substring + smaller
                    string = ans_string + substring + ans_string[::-1]
                    print(string)
                    return
        
        elif len(s) == 1:
            string = ans_string + s[0] + ans_string[::-1]
            print(string)
            return

        else:
            print(ans_string + ans_string[::-1])
            return

        
        
            
        


    
for _ in range(oi()):
    solve()