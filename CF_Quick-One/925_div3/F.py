from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N, K = map(int, input().split())
    
    first = list(map(int, input().split()))
    e = first[0]
    first = first[1:]
    index_map = {}
    for index, element in enumerate(first):
        index_map[element] = index
    lower_e = []
    upper_e = []
    
    flag = True
    
    for _ in range(K - 1):
        if not flag:
            input()
            continue
        
        inp = list(map(int, input().split()))
        s = inp[0]
        rest = inp[1:]
        
        a = []
        for i in range(len(rest)):
            if rest[i] in index_map:
                a.append(index_map[rest[i]])
                rest[i] = index_map[rest[i]]
            else:
                index_e = i
        # check if a is in sorted order
        if len(a) != 0:
            for i in range(1, len(a)):
                if a[i] < a[i - 1]:
                    flag = False
                    break
                    
        if index_e + 1 < len(rest):
            upper_e.append(rest[index_e + 1])
        if index_e - 1 >= 0:
            lower_e.append(rest[index_e - 1])
    

    if len(lower_e) != 0 and len(upper_e) != 0:
        if min(upper_e) - max(lower_e) <= 0:
            flag = False
    
    if flag:
        print("YES")
    else:
        print("NO")
        

for _ in range(int(input())):
    solve()