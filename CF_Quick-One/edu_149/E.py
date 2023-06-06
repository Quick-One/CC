from sys import stdin
def input(): return stdin.readline()[:-1]
MOD = 998244353
 
N = int(input())
arr = list(map(int, input().split()))
 
A = [-1] * (2 ** N)
for seed, element in enumerate(arr):
    if element == -1:
        continue
    A[element - 1] = seed
 
if N == 0:
    print(1)
    exit()
 
layersize = 1
divisor = 2 ** N
ans = 1
previous_layer = None
to_compute = []
for layer_no in range(1, N+1):

    layersize = layersize << 1
    divisor = divisor >> 1
    layer = [-1] * layersize
 
    old_elements = layersize >> 1
 
    for element in range(old_elements):
        if A[element] == -1:
            continue
 
        coord = A[element] // divisor
        if layer[coord] != -1:
            print(0)
            exit()
        else:
            layer[coord] = element
    floating = 0
    for element in range(old_elements, layersize): 
    
        if A[element] == -1:
            floating += 1
            continue
 
        coord = A[element] // divisor
        if layer[coord] != -1:
            print(0)
            exit()
        else:
            layer[coord] = element


    if layer_no== 1:
        empty = layer.count(-1)
        if empty == 2:
            ans = (ans * 2) % MOD
    else:
        for i in range(old_elements):
            if previous_layer[i] == -1:
                l = 2 * i
                r = 2 * i + 1
                k = 0
                if layer[l] == -1:
                    k += 1
                if layer[r] == -1:
                    k += 1
                if k == 0:
                    print(0)
                    exit()
                ans = (ans * k) % MOD
    to_compute.append(floating)
    previous_layer = layer
 
M = max(to_compute)
factorial = [1] * (M + 1)
for i in range(1, M+1):
    factorial[i] = (factorial[i-1] * i) % MOD
 
for floating in to_compute:
    ans = (ans * factorial[floating]) % MOD
print(ans)