from sys import stdin
def input(): return stdin.readline()[:-1]
from random import choice

def ask(a):
    print('? {}'.format(a), flush=True)
    inp = input().strip()
    if inp == '>':
        return 1
    elif inp == '<':
        return -1
    elif inp == '=':
        return 0
    else:
        exit()
    
def answer(arr):
    print('! {}'.format(' '.join(map(str, arr))), flush=True)

ANS = [0] * 2001

def quicksort(l, r, indices):

    if len(indices) == 0: return
    if l == r:
        ANS[indices[0]] = l
        return

    pivot = choice(indices)
    while ask(pivot): pass
    left = []
    right = []
    
    for i in indices:
        if i == pivot: continue
        if ask(i) == 1:
            right.append(i)
        else:
            left.append(i)
        ask(pivot)
    
    ANS[pivot] = l + len(left)
    quicksort(l, l + len(left) - 1, left)
    quicksort(l + len(left) + 1, r, right)
    

def solve():
    N = int(input())
    quicksort(1, N, list(range(1, N+1)))
    answer(ANS[1:N+1])

for _ in range(int(input())):
    solve()