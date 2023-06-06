def oi():
    return int(input())

def ti():
    return map(int, input().split())

def mi():
    return list(map(int, input().split()))

def solve():
    n = oi()
    string = input().strip()

    forward = [0] * n
    backward = [0] * n

    forward_set = set()
    forward_count = 0
    backward_set = set()
    backward_count = 0

    for i in range(n):
        if string[i] not in forward_set:
            forward_set.add(string[i])
            forward_count += 1
        forward[i] = forward_count
    
    for i in range(n-1, -1, -1):
        if string[i] not in backward_set:
            backward_set.add(string[i])
            backward_count += 1
        backward[i] = backward_count
    
    # print(forward)
    # print(backward)

    ans = -1
    for i in range(n-1):
        ans = max(ans, forward[i] + backward[i+1])
    print(ans)

for _ in range(oi()):
    solve()