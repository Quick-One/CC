from sys import stdin
def input(): return stdin.readline()[:-1]


def equal_subarray(array):
    n = len(array)
    s = sum(array)
    if s % 2 == 1:
        return False, None
    s //= 2

    DP = [[False] * (s + 1) for _ in range(n + 1)]
    DP[0][0] = True
    for i in range(1, n + 1):
        for j in range(s + 1):
            DP[i][j] = DP[i - 1][j]
            if j - array[i - 1] >= 0:
                DP[i][j] |= DP[i - 1][j - array[i - 1]]
    if not DP[n][s]:
        return False, None

    indices = []
    i, j = n, s
    while i > 0 and j > 0:
        if DP[i - 1][j]:
            i -= 1
        else:
            indices.append(i - 1)
            j -= array[i - 1]
            i -= 1
    return True, indices


def tell(a):
    print(a, flush=True)
    return int(input())


N = int(input())
A = list(map(int, input().split()))
boolean, res = equal_subarray(A)

if not boolean:
    print('First', flush=True)
    non_zero = set(range(N))

    while True:
        my_choice = next(iter(non_zero))
        opponesnt_choice = tell(my_choice + 1)
        if opponesnt_choice == -1 or opponesnt_choice == 0:
            exit()
        opponesnt_choice -= 1
        d = min(A[my_choice], A[opponesnt_choice])
        A[my_choice] -= d
        A[opponesnt_choice] -= d
        if A[my_choice] == 0:
            non_zero.remove(my_choice)
        if A[opponesnt_choice] == 0:
            non_zero.remove(opponesnt_choice)
else:
    print('Second', flush=True)
    partition1 = set(res)
    partition2 = set(range(N)) - partition1
    while True:
        # print(*A, flush=True)
        opponesnt_choice = int(input())
        if opponesnt_choice == -1 or opponesnt_choice == 0:
            exit()
        opponesnt_choice -= 1
        if opponesnt_choice in partition1:
            my_choice = next(iter(partition2))
        else:
            my_choice = next(iter(partition1))
        d = min(A[my_choice], A[opponesnt_choice])
        A[my_choice] -= d
        A[opponesnt_choice] -= d
        if A[my_choice] == 0:
            partition1.discard(my_choice)
            partition2.discard(my_choice)
        if A[opponesnt_choice] == 0:
            partition1.discard(opponesnt_choice)
            partition2.discard(opponesnt_choice)
        print(my_choice + 1, flush=True)
