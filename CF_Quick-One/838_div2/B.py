for _ in range(int(input())):
    n = int(input())
    l = [list(i) for i in enumerate(map(int, input().split()))]
    l.sort(key = lambda x: x[1])
    soln = []

    for i in range(1, n):
        index, val = l[i]
        _, val_b = l[i-1]
        addent = (val_b-val)%val_b
        if addent == 0:
            continue
        l[i][1] += addent
        soln.append((index+1, addent))

    print(len(soln))
    for i in soln:
        print(*i)