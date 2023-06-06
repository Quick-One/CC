def solve():
    _, atack = map(int,input().split())
    h = list(map(int,input().split()))
    p = list(map(int,input().split()))
    a = sorted(list(i) for i in zip(p,h))
    cum_atack = 0
    pointer = 0
    while (atack > 0):
        cum_atack += atack
        while (pointer < len(a) and a[pointer][1] <= cum_atack):
            pointer += 1
        if pointer == len(a):
            break
        atack -= a[pointer][0]
    if pointer == len(a):
        print("YES")
    else:
        print("NO")

for _ in range(int(input())):
    solve()