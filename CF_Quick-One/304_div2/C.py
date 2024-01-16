from sys import stdin, stdout
def input(): return stdin.readline()[:-1]

from collections import deque

states = set()

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

a = [A[i] - 1 for i in range(1, len(A))]
b = [B[i] - 1 for i in range(1, len(B))]
a.reverse()
b.reverse()
a = deque(a)
b = deque(b)

def HASH(arr1, arr2):
    h1 = arr1[0]
    h2 = arr2[0]
    
    for i in range(1, len(arr1)):
        h1 = h1 * 10 + arr1[i]
    
    for i in range(1, len(arr2)):
        h2 = h2 * 10 + arr2[i]
    
    return h1 * 10 ** 10 + h2

HITS = 0
states.add(HASH(a, b))

while True:
    if a[-1] > b[-1]:
        a.appendleft(b.pop())
        a.appendleft(a.pop())
    else:
        b.appendleft(a.pop())
        b.appendleft(b.pop())
    HITS += 1
    
    if len(a) == 0 or len(b) == 0:
        break
    
    STATE = HASH(a, b)
    if STATE in states:
        print(-1)
        exit()
    states.add(STATE)
    

if len(a) == 0: print(HITS, 2)
else: print(HITS, 1)