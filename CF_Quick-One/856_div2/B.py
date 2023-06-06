def solve():
    N = int(input())
    arr = list(map(int, input().split()))
    arr[0] += 2

    for i in range(1, N):
        l = []
        element = arr[i]
        for k in (element, element + 1, element + 2):
            if k % arr[i-1]:
                l.append(k)
        arr[i] = max(l)

    print(*arr)

def main():
    for _ in range(int(input())):
        solve()

main()