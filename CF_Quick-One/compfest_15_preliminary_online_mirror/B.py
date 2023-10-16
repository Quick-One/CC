from sys import stdin
def input(): return stdin.readline()[:-1]

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
M = int(input())
C = list(map(int, input().split()))
D = list(map(int, input().split()))

d1 = {A[i]: B[i] for i in range(N)}
d2 = {C[i]: D[i] for i in range(M)}

MOD =  998244353

ans = 0
for prime in d2:
    if (prime not in d1) or (d1[prime] - d2[prime]) < 0 :
        print(0)
        exit()


for prime in d1:
    if prime in d2:
        if d1[prime] != d2[prime]:
            ans += 1
    else:
        ans += 1
print(pow(2, ans, MOD))