from random import randint
from collections import Counter


MODS = [10**9+7, 10**9+9, 998244353]
K = len(MODS)

BASES = []
for mod in MODS:
    base = randint(2, mod-1)
    BASES.append(base)

def add(hash1, hash2, mod):
    ans = [0]*K
    for i in range(K):
        ans[i] = (hash1[i] + hash2[i]) % mod[i]
    return ans
    
def sub(hash1, hash2, mod):
    ans = [0]*K
    for i in range(K):
        ans[i] = (hash1[i] - hash2[i]) % mod[i]
    return ans

def mul(hash1, bases, mod):
    ans = [0]*K
    for i in range(K):
        ans[i] = (hash1[i] * bases[i]) % mod[i]
    return ans

def add1(hash1, mod):
    ans = [0]*K
    for i in range(K):
        ans[i] = (hash1[i] + 1) % mod[i]
    return ans

N = int(input())
arr = list(map(int, input().split()))
graph = {}
for _ in range(N-1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)

C = Counter(arr)
HashI = [0]*K
BaseMul = [1]*K
for i in range(N):
    count = C[i]
    for j in range(K):
        HashI[j] += count*BaseMul[j]
        HashI[j] %= MODS[j]
        BaseMul[j] *= BASES[j]
        BaseMul[j] %= MODS[j]

# DFS1
s1 = []
s1.append(0)
visited1 = [False]*N
visited1[0] = True
parent1 = [-1]*N
order = []
while s1:
    curr = s1.pop()
    order.append(curr)
    visited1[curr] = True
    for child in graph[curr]:
        if not visited1[child]:
            s1.append(child)
            parent1[child] = curr

dp1 = [0]*N
for parent in reversed(order):
    parent_h = [0]*K
    for child in graph[parent]:
        if child == parent1[parent]:
            continue
        child_h = dp1[child]
        child_h = mul(child_h, BASES, MODS)
        parent_h = add(parent_h, child_h, MODS)
    parent_h = add1(parent_h, MODS)
    dp1[parent] = parent_h

# DFS2
dp2 = [0]*N
dp2[0] = [0]*K
for child in order:
    parent = parent1[child]
    if parent == -1:
        continue
    ans = [0]*K
    ans = add(ans, dp1[parent], MODS)
    ans = sub(ans, mul(dp1[child], BASES, MODS), MODS)
    ans = add(ans, mul(dp2[parent], BASES, MODS), MODS)
    dp2[child] = ans

valid_hashes = set()
prod = [1]*K
for i in range(N):
    valid_hashes.add(tuple(add(HashI, prod, MODS)))
    prod = mul(prod, BASES, MODS)

ans_nodes = []
for node in range(N):
    node_hash = add(dp1[node], mul(dp2[node], BASES, MODS), MODS)
    if tuple(node_hash) in valid_hashes:
        ans_nodes.append(node+1)

print(len(ans_nodes))
print(*ans_nodes)