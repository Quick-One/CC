def oi():
    return int(input())
 
def ti():
    return map(int, input().split())
 
def mi():
    return list(map(int, input().split()))
 
def solve():
    N = oi()
    A = mi()

    d = {}
    for i in A:
        d[abs(i)] = d.get(abs(i), 0) + 1
    
    pairs = 0
    singles = 0
    for i in d.values():
        if i == 2:
            pairs += 1
        elif i == 1:
            singles += 1
    

    arr1 = list(range(1, pairs+singles+1))
    l = arr1[-1]
    for i in range(pairs):
        arr1.append(l-1)
        l-=1
    print(*arr1)

    arr2 = []
    for i in range(pairs):
        arr2.append(1)
        arr2.append(0)
    for i in range(singles):
        arr2.append(i+1)
    print(*arr2)
    
for _ in range(oi()):
    solve()