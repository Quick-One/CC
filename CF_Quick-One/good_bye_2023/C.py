from sys import stdin
def input(): return stdin.readline()[:-1]



def fucn(even, odd):
    if even + odd == 1:
        return 0
    # (n-1) - 2*floor((n-1)/3).
    
    odd -= 1
    return (odd - 1) - 2 * ((odd - 1)//3)

def solve():
    N = int(input())
    Arr=  list(map(int,input().split()))
    
    odd = 0
    even = 0
    
    ANS = []
    cumsum = 0
    for i in Arr:
        if i%2==0:
            even+=1
        else:
            odd+=1
        cumsum += i
        ANS.append(cumsum - fucn(even,odd))
    print(*ANS)
        
        

for _ in range(int(input())):
    solve()