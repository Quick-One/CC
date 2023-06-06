def f(mid, arr, size):
    return arr[mid] >= size - mid

def solve():
    N = int(input())
    arr= list(map(int, input().split()))

    ans = []
    for hi in range(N):
        size = hi+1
        low = 0
        while low < hi:
            mid = low + (hi - low) // 2
            if f(mid, arr, size):
                hi = mid
            else:
                low = mid + 1
        ans.append(size - low)
    print(*ans)


def main():
    for _ in range(int(input())):
        solve()

main()