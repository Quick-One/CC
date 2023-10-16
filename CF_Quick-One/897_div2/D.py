from sys import stdin
def input(): return stdin.readline()[:-1]




def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [i-1 for i in A]

    if K == 1:
        for i in range(N):
            if A[i] != i:
                print('NO')
                return
        print('YES')
        return

    cycle_sizes = []
    global_visited = set()
    for node in range(N):
        if node in global_visited:
            continue

        order_no = 0
        visited = {node: 0}
        global_visited.add(node)
        while True:
            order_no += 1
            node = A[node]
            if node in global_visited:
                if node in visited:
                    cycle_sizes.append(order_no - visited[node])
                break
            else:
                global_visited.add(node)
                visited[node] = order_no
    
    if len(set(cycle_sizes)) == 1 and cycle_sizes[0] == K:
        print('YES')
    else:
        print('NO')




for _ in range(int(input())):
    solve()