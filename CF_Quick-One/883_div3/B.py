from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    rows = []
    for _ in range(3):
        rows.append(input().strip())

    for r in rows:
        if len(set(r)) == 1 and r[0] != '.':
            print(r[0])
            return
    
    for c in range(3):
        if rows[0][c] == rows[1][c] == rows[2][c] and rows[0][c] != '.':
            print(rows[0][c])
            return
    
    if rows[0][0] == rows[1][1] == rows[2][2] and rows[0][0] != '.':
        print(rows[0][0])
        return
    
    if rows[0][2] == rows[1][1] == rows[2][0] and rows[0][2] != '.':
        print(rows[0][2])
        return
    
    print('DRAW')


for _ in range(int(input())):
    solve()
