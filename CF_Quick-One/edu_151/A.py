from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N, K, X = map(int, input().split())
    if X != 1:
        print("YES")
        ANS = [1] * N
        print(len(ANS))
        print(*ANS)
    else:
        if K == 1:
            print("NO")
        else:
            if N%2 == 0:
                print("YES")
                ANS = [2] * (N//2)
                print(len(ANS))
                print(*ANS)
            else:
                if K == 2:
                    print("NO")
                else:
                    if N == 1:
                        print("NO")
                    else:
                        print("YES")
                        ANS = [3] + (N-3)//2 * [2]
                        print(len(ANS))
                        print(*ANS)


for _ in range(int(input())):
    solve()