from sys import stdin
def input(): return stdin.readline()[:-1]

def oi():
    return int(input())
 
def ti():
    return map(int, input().split())
 
def mi():
    return list(map(int, input().split()))
 
from collections import Counter
def solve():
    N = oi()
    string = input().strip()

    char = 'z'
    for i in string:
        char = min(char, i)
    c = Counter(string)
    # print(char)
    count = c[char]

    if count == 1:
        if string[0] == char:
            print(string)
        else:
            rigth_most_index = string.rfind(char)
            new_string = char
            new_string += string[:rigth_most_index]
            new_string += string[rigth_most_index+1:]
            print(new_string)
    else:
        rigth_most_index = string.rfind(char)
        new_string = char
        new_string += string[:rigth_most_index]
        new_string += string[rigth_most_index+1:]
        print(new_string)


    
for _ in range(oi()):
    solve()