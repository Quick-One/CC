from sys import stdin
def input(): return stdin.readline()[:-1]

def finder(string):
    cnt00 = 0
    cnt11 = 0

    for i in range(0, len(string) - 1):
        if string[i] == '0' and string[i + 1] == '0':
            cnt00 += 1
        elif string[i] == '1' and string[i + 1] == '1':
            cnt11 += 1

    return cnt00, cnt11

def solve():
    n, m = map(int, input().split())
    s = input()
    t = input()

    cnt00, cnt11 = finder(s)


    
    if sum(finder(t)) ==  0:
        flag = True
    else:
        flag = False

    if cnt00 == 0:
        if cnt11 == 0:
            print('YES')
            return
        else:
            if len(t) %2 == 1 and t[0] == '0' and flag:
                print('YES')
                return
            else:
                print('NO')
                return
    
    else:
        if cnt11 == 0:
            if len(t) %2 == 1 and t[0] == '1' and flag:
                print('YES')
                return
            else:
                print('NO')
                return
        else:
            print("NO")
            return
    


for _ in range(int(input())):
    solve()