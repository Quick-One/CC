from sys import stdin
def input(): return stdin.readline()[:-1]

def solve():
    N = int(input())
    arr = list(map(int, input().split()))

    index = arr.index(N)

    if N == 1:
        print(" ".join(map(str, arr)))
        return
    
    if N == 2:
        print(" ".join(map(str, arr[::-1])))
        return

    if index == 0:
        index2 = arr.index(N - 1)
        potential_soln = [-1] * N
        for point in range(index2):
            a = arr[index2:] + arr[point:index2][::-1] + arr[:point]
            potential_soln = max(potential_soln, a)
        if index2 != N-1:
            print(" ".join(map(str, potential_soln)))
        else:
            for point in range(N):
                a = arr[point:][::-1] + arr[:point]
                potential_soln = max(potential_soln, a)
            print(" ".join(map(str, potential_soln)))


    elif index == N - 1:
        potential_soln = [-1] * N
        for point in range(N-2):
            a = [N] + arr[point:N- 1][::-1] + arr[:point]
            potential_soln = max(potential_soln, a)
        for point in range(N):
            a = arr[point:][::-1] + arr[:point]
            potential_soln = max(potential_soln, a)
        print(" ".join(map(str, potential_soln)))

    elif index == 1:
        ans_arr = arr[index:]
        ans_arr.append(arr[0])
        print(" ".join(map(str, ans_arr)))
    else:
        ans_arr = arr[index:]
        ans_arr.append(arr[index - 1])
        start = index - 2

        while arr[start] > arr[0]:
            ans_arr.append(arr[start])
            start -= 1
        
        ans_arr.extend(arr[:start + 1])
        print(" ".join(map(str, ans_arr)))
 
for _ in range(int(input())):
    solve()