from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    # N = int(input())
    N, K = map(int, input().split())
    Arr = list(map(int, input().split()))
    
    prod = 1
    for i in range(N):
        prod *= Arr[i]
        
    if prod > 2023:
        print("NO")
        return
    
    if 2023 % prod != 0:
        print("NO")
        return
    
    print("YES")
    aloha = 2023 // prod
    ANS = [aloha]
    for _ in range(K-1):
        ANS.append(1)
    print(*ANS)
    

for _ in range(int(input())):
    solve()