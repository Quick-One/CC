def one_input():
    return int(input())

def two_input():
    return map(int, input().split())

def many_input():
    return list(map(int, input().split()))

def solve():
    s = one_input()
    arr = many_input()

    even = []
    odd = []

    for index, elem in enumerate(arr):
        if elem % 2 == 0:
            even.append((index, elem))
        else:
            odd.append((index, elem))

    if len(even) >= 2 and len(odd)>= 1:
        print("YES")
        even = even[:2]
        odd = odd[:1]
        for i in even:
            print(i[0]+1, end=" ")
        for i in odd:
            print(i[0]+1, end=" ")
        print()

    elif len(odd)>=3:
        print("YES")
        odd = odd[:3]
        for i in odd:
            print(i[0]+1, end=" ")
        print()
    else:
        print("NO")
for _ in range(one_input()):
    solve()