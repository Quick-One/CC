from sys import stdin
def input(): return stdin.readline()[:-1]

from collections import Counter

def are_same(prev, new):
    # check if 2 Counter objects are the same
    if len(prev) != len(new):
        return False

    for k in prev:
        if k not in new:
            return False
        if prev[k] != new[k]:
            return False
    return True

def find_diff(prev, new):
    for i in range(1, 10):
        if (new[i] - prev[i]) == 1:
            return i

def remove(arr):
    s = f'- {len(arr)} {" ".join(map(str, arr))}'
    print(s, flush=True)

def answer(a):
    print('! {}'.format(a), flush=True)

def solve():
    N = int(input()) 

    cnt = None
    while True:
        state = list(map(int, input().split()))
        
        if len(state) == 1:
            answer(1)
            return

        if cnt is None:
            cnt = Counter(state)
            remove([])
        
        else:
            new_cnt = Counter(state)
            if are_same(cnt, new_cnt):
                remove([])
            else:
                diff = find_diff(cnt, new_cnt)
                d = [diff] * (new_cnt[diff])

                if new_cnt[diff] == 1:
                    for i in range(len(state)):
                        if state[i] == diff:
                            answer(i+1)
                            return

                cnt = Counter(d)
                arr = []
                for i in range(len(state)):
                    if state[i] != diff:
                        arr.append(i+1)
                remove(arr)
for _ in range(int(input())):
    solve()
