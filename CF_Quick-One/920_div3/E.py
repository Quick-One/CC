from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    # N = int(input())
    h,w, xa, ya, xb, yb = map(int, input().split())
    if (xb - xa <= 0):
        print("Draw")
        return
    
    if (xb - xa) % 2 == 1:
        moves = (xb - xa - 1) // 2
        blk_rangex, blk_rangey = max(1, yb - moves), min(w, yb + moves)
        white_rangex, white_rangey = max(1, ya - moves - 1), min(w, ya + moves + 1)
        
        if white_rangex <= blk_rangex <= blk_rangey <= white_rangey:
            print("Alice")
        else:
            print("Draw")
    else:
        moves = (xb - xa) // 2
        blk_rangex, blk_rangey = max(1, yb - moves), min(w, yb + moves)
        white_rangex, white_rangey = max(1, ya - moves), min(w, ya + moves)
        if blk_rangex <= white_rangex <= white_rangey <= blk_rangey:
            print("Bob")
        else:
            print("Draw")

for _ in range(int(input())):
    solve()