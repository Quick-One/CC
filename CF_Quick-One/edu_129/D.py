from sys import stdin
def input(): return stdin.readline()[:-1]

N, x = map(int, input().split())

from collections import deque
threshold = 10 ** N

d = {}
q = deque()

d[x] = 0
q.append(x)

while q:
    node = q.popleft()
    
    string = str(node)
    
    if len(string) == N:
        print(d[node])
        exit()
    
    for dig in string:
        if dig == '0': continue
        dig = int(dig)
        res = dig * node
        if res < threshold:
            if res not in d:
                d[res] = d[node] + 1
                q.append(res)
            else:
                d[res] = min(d[res], d[node] + 1)

print(-1)