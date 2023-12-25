from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N = int(input())
    Arr = list(map(int, input().split()))

    mini = min(Arr)
    index = Arr.index(mini)

    Arr2 = Arr[index+1:]
    if Arr2 != sorted(Arr2):
        print(-1)
        return
    
    print(index)


for _ in range(int(input())):
    solve()