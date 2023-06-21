from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    n, m, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    stack = arr[::-1]
    other_spaces = set()

    free_space = m * n - 2

    for i in range(k, 0, -1):
        if i in other_spaces:
            other_spaces.remove(i)
            free_space += 1
        else:
            while stack[-1] != i:
                if free_space > 0:
                    other_spaces.add(stack.pop())
                    free_space -= 1
                else:
                    print('TIDAK')
                    return
            if free_space >= 2:
                stack.pop()
            else:
                print('TIDAK')
                return
    print('YA')



for _ in range(int(input())):
    solve()