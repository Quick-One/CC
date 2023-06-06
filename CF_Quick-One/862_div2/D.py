from sys import stdin
def input(): return stdin.readline()[:-1]

graph = {}
N = int(input())
for _ in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []
    graph[a].append(b)
    graph[b].append(a)

from collections import deque
bfs_queue = deque()
bfs_queue.append(0)

visited = [False]*N
visited[0] = True
parent = [-1]*N
dist = [0]*N
while bfs_queue:
    node = bfs_queue.popleft()
    for i in graph[node]:
        if not visited[i]:
            visited[i] = True
            parent[i] = node
            dist[i] = dist[node] + 1
            bfs_queue.append(i)
farthest_node = dist.index(max(dist))

bfs_queue.append(farthest_node)
visited = [False]*N
visited[farthest_node] = True
parent = [-1]*N
dist = [0]*N
while bfs_queue:
    node = bfs_queue.popleft()
    for i in graph[node]:
        if not visited[i]:
            visited[i] = True
            parent[i] = node
            dist[i] = dist[node] + 1
            bfs_queue.append(i)

farthest2 = dist.index(max(dist))
path = [farthest2]
while path[-1] != farthest_node:
    path.append(parent[path[-1]])
middle_node = path[len(path)//2]
bfs_queue.append(middle_node)
visited = [False]*N
visited[middle_node] = True
parent = [-1]*N
DIST = [0]*N
while bfs_queue:
    node = bfs_queue.popleft()
    for i in graph[node]:
        if not visited[i]:
            visited[i] = True
            parent[i] = node
            DIST[i] = DIST[node] + 1
            bfs_queue.append(i)
root = DIST.index(max(DIST))
# print(root+1)
path = [root]
while path[-1] != middle_node:
    path.append(parent[path[-1]])

bfs_queue.append(path[-2])
visited = [False]*N
visited[path[-2]] = True
parent = [-1]*N
dist = [0]*N
dist[path[-2]] = 1
while bfs_queue:
    node = bfs_queue.popleft()
    for i in graph[node]:
        if not visited[i] and i != path[-1]:
            visited[i] = True
            parent[i] = node
            dist[i] = dist[node] + 1
            bfs_queue.append(i)

main_level_dict = {}
for i in dist:
    if i == 0:
        continue
    if i not in main_level_dict:
        main_level_dict[i] = 0
    main_level_dict[i] += 1


others = {}
for i in range(N):
    if visited[i]:
        continue
    key = DIST[i]
    if key not in others:
        others[key] = 0
    others[key] += 1
# print(others)
# print(main_level_dict)

ANS = [N] * N
main_level_dict_p = max(main_level_dict)
others_p = max(others)
length_longest = max(main_level_dict) + max(others)
clump_size = 0
while length_longest > 0:
    if main_level_dict_p in main_level_dict:
        clump_size += main_level_dict[main_level_dict_p]
    if others_p in others:
        clump_size += others[others_p]
    ANS[length_longest-1] = N - clump_size + 1
    main_level_dict_p -= 1
    others_p -= 1
    length_longest -= 1

print(*ANS)