from sys import stdin
def input(): return stdin.readline()[:-1]
from collections import defaultdict
from collections import deque


def solve():
    string = input().strip()

    current_node = 0
    node_count = 0
    total = string.count('+')
    parent = [-1] * (total + 1)

    d  = defaultdict(set)
    g = defaultdict(list)

    for i in string:
        if i == '+':
            papa = current_node
            node_count += 1
            next_node = node_count
            parent[next_node] = papa
            g[papa].append(next_node)
            g[next_node].append(papa)
            current_node = next_node
        elif i == '-':
            current_node = parent[current_node]
        else:
            query = int(i)
            d[current_node].add(query)
    

    level = [-1] * (total + 1)
    level[0] = 0
    visited = [False] * (total + 1)
    bfs_queue = deque([0])
    order = [0]

    while bfs_queue:
        node = bfs_queue.popleft()
        for child in g[node]:
            if not visited[child]:
                visited[child] = True
                level[child] = level[node] + 1
                bfs_queue.append(child)
                order.append(child)

    state = [0] * (total + 1)

    for node in reversed(order):
        if state[node] or (1 in d[node]) or level[node] <= 1:
            state[node] = 1
        
        if state[node] == 1:
            papa = parent[node]
            if papa != -1:
                state[papa] = 1
    # print(state)
    for node in range(total + 1):
        if 0 in d[node] and state[node] == 1:
            print('NO')
            return
    print('YES') 


for _ in range(int(input())):
    solve()