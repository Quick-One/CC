def oi():
    return int(input())
 
def ti():
    return map(int, input().split())
 
def mi():
    return list(map(int, input().split()))
 
from collections import Counter, defaultdict
from string import ascii_lowercase

def solve():
    N, K = ti()
    string = input().strip()

    if N == 1:
        print(0)
        return

    counter = defaultdict(int)
    for char in string:
        counter[char] += 1
    
    # print(counter)
    
    curr_ans = 0
    for l in ascii_lowercase:
        u = l.upper()
        curr_ans += min(counter[l], counter[u])
    # print(curr_ans)

    best_ans = 0
    for l in ascii_lowercase:
        u = l.upper()
        best_ans += (counter[l] + counter[u]) // 2
    
    # print(best_ans)
    print(min(curr_ans + K, best_ans))

    
for _ in range(oi()):
    solve()