from sys import stdin
from collections import defaultdict, Counter, deque
from math import log, atan 
from random import randint as random

def input(): return stdin.readline()[:-1]

random_int = random(100, 10**9)

def solve():
    N = int(input())
    graph = defaultdict(list)
    for _ in range(N-1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)

    bfs = deque()
    stack = []
    directed_graph = defaultdict(list)

    bfs.append((0, -1))
    stack.append(0)

    while bfs:
        node, parent = bfs.popleft()
        for child in graph[node]:
            if child != parent:
                bfs.append((child, node))
                stack.append(child)
                directed_graph[node].append(child)
    
    symmetric = [None] * N
    
    hash_dp = [0] * N
    hash_dict = {}
    cnt = 0

    for node in reversed(stack):
        children = directed_graph[node]
        children_hashes = [hash_dp[child] for child in children]
        children_hashes.sort()

        key = tuple(children_hashes)
        if key in hash_dict:
            hash_dp[node] = hash_dict[key]
        else:
            hash_dict[key] = cnt
            hash_dp[node] = cnt
            cnt += 1

        if len(children) == 0:
            symmetric[node] = True
            continue
            
        children_hashes = Counter(children_hashes)
        odd_node_hash = None
        for hashOFchild, count in children_hashes.items():
            if count % 2 == 1:
                if odd_node_hash != None:
                    symmetric[node] = False
                    break
                odd_node_hash = hashOFchild
        else:
            if odd_node_hash == None:
                symmetric[node] = True
            else:
                for child in children:
                    if hash_dp[child] == odd_node_hash:
                        symmetric[node] = symmetric[child]
                        break
    
    print("YES" if symmetric[0] else "NO")

def main():
    for _ in range(int(input())):
        solve()

main()