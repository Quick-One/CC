from sys import stdin
def input(): return stdin.readline()[:-1]


MAXN = 10 ** 6 + 5
seive = [i for i in range(MAXN)]

for i in range(2, MAXN):
    if seive[i] == i:
        for j in range(i, MAXN, i):
            seive[j] = i


primes = []
for i in range(2, MAXN):
    if seive[i] == i:
        primes.append(i)

d = {}
for i, p in enumerate(primes):
    d[p] = i

def get_factors(n):
    factors = []
    while n > 1:
        factors.append(seive[n])
        n //= seive[n]
    return factors

def get_state(num):
    d = {}
    for f in get_factors(num):
        d[f] = d.get(f, 0) + 1
    return d

def num_facs(state):
    ans = 1
    for _, e in state.items():
        ans *= (e + 1)  
    return ans

def solve():
    N, Q = map(int, input().split())
    defau = N
    state_N = get_state(N)
    copy=state_N.copy()
    ## finding the first prime not in the state

    for _ in range(Q):
        query = list(map(int, input().split()))
        if len(query) == 2:
            x = query[1]
            N *= x
            
            state_x = get_state(x)
            for p, e in state_x.items():
                state_N[p] = state_N.get(p, 0) + e
            D = num_facs(state_N)
            
            if N % D == 0:
                print('YES')
            else:
                print('NO')
        else:
            N = defau
            state_N = copy.copy()


for _ in range(int(input())):
    solve()