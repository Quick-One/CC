def oi():
    return int(input())
 
def ti():
    return map(int, input().split())
 
def mi():
    return list(map(int, input().split()))
 
def solve():
    letters = ['m', 'e', 'o', 'w']
    n = oi()
    string = input().strip().lower()

    for chars in letters:
        if chars.lower() not in string:
            print('No')
            return

    for char in string:
        char = char.lower()
        if char not in letters:
            print('No')
            return
        index = letters.index(char)
        letters = letters[index:]
    print('Yes')

    
for _ in range(oi()):
    solve()