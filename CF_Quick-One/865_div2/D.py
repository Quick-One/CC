from collections import deque, defaultdict
from sys import stdin
def input(): return stdin.readline()[:-1]


def query1(x):
    print(f'+ {x}', flush=True)
    out = int(input())
    if out == -2:
        exit()


def query2(a, b):
    print(f'? {a} {b}', flush=True)
    out = int(input())
    if out == -2:
        exit()
    return out


def response(arr, arr2):
    string = ' '.join(map(str, arr))
    string2 = ' '.join(map(str, arr2))
    ans_string = string + ' ' + string2
    print(f'! {ans_string}', flush=True)
    verdict = int(input())
    if verdict == -2:
        exit()


def solve():
    N = int(input())
    query1(N+1)
    query1(N)

    graph = [[] for _ in range(N+1)]

    X = N
    for node1 in range(1, N+1):
        node2 = X - node1
        if 1 <= node2 <= N:
            if node2 not in graph[node1] and node2 != node1:
                graph[node1].append(node2)
            if node1 not in graph[node2] and node1 != node2:
                graph[node2].append(node1)

    X = N+1
    for node1 in range(1, N+1):
        node2 = X - node1
        if 1 <= node2 <= N:
            if node2 not in graph[node1] and node2 != node1:
                graph[node1].append(node2)
            if node1 not in graph[node2] and node1 != node2:
                graph[node2].append(node1)

    bfs = deque()
    visited = [False] * (N+1)
    start = N
    bfs.append(start)
    visited[start] = True
    forward = []
    while bfs:
        node = bfs.popleft()
        forward.append(node)
        for child in graph[node]:
            if not visited[child]:
                visited[child] = True
                bfs.append(child)
    # print(forward)

    depth_dict = defaultdict(list)
    i = 1
    for j in range(2, N+1):
        depth = query2(i, j)
        depth_dict[depth].append(j)
    # print(depth_dict)
    deep = max(depth_dict.keys())
    deep = depth_dict[deep][0]
    alpha = [0] * N
    alpha[0] = deep
    for i in range(1, N+1):
        if i == deep:
            continue
        d = query2(deep, i)
        alpha[d] = i

    l = list(zip(alpha, forward))
    l.sort()
    r = [x[1] for x in l]
    ans1 = r

    l = list(zip(alpha, forward[::-1]))
    l.sort()
    r = [x[1] for x in l]
    ans2 = r
    response(ans1, ans2)


t = int(input())
for _ in range(t):
    solve()
# exit()