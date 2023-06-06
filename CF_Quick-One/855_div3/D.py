def oi():
    return int(input())
 
def ti():
    return map(int, input().split())
 
def mi():
    return list(map(int, input().split()))
 
def solve():
    n = oi()
    string = input().strip()

    s = ''
    count = 0
    temp = []
    
    for char in string:
        if char != s:
            if s != '':
                temp.append((s, count))
            s = char
            count = 1
        else:
            count += 1
    temp.append((s,count))

    total = n - 1
    for c, i in temp:
        if i > 1:
            total -= i - 2


    # finding lenggths of alternating sequences
    al_len = []
    s = ''
    for char in string:
        if len(s) <= 1:
            s += char
        else:
            if char == s[-2]:
                s += char
            else:
                if len(s) > 2 and len(set(s)) == 2:
                    al_len.append(s)
                s = s[-1] + char
    if len(s) > 2 and  len(set(s)) == 2 :
        al_len.append(s)
    al_len_len = []
    for i in al_len:
        al_len_len.append(len(i))
    for i in al_len_len:
        if i > 2:
            total -= i - 2
    # print(al_len)


        



    print(total)

    
for _ in range(oi()):
    solve()