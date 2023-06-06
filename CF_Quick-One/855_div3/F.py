from collections import defaultdict
from sys import stdin
 
def input(): return stdin.readline()[:-1]
 
 
n = int(input())
strings = []
for _ in range(n):
    s = [ord(i)-97 for i in input()]
    XOR = 0 # Determines the parity of fequency of each character
    OR = 0 # Determines the presence of each character
    for i in s:
        XOR ^= 1 << i
        OR |= 1 << i
    strings.append((XOR, OR))
 
ans = 0
for i in range(26):
    
    # Making a list of those numbers which do not contain the character
    use = []
    for xor_mask, or_mask in strings:
        if (or_mask >> i) & 1:
            continue
        use.append(xor_mask)
    
    # 1111111111111i111111111111 where i is 0 mask
    mask = (1 << 26)-1-(1 << i)
    
    cnt = defaultdict(int) 
    for xor_mask in use:
        cnt[xor_mask] += 1
    
    i_ans = 0
    for XOR_mask in list(cnt.keys()):
        i_ans += cnt[XOR_mask] * cnt[mask - XOR_mask]
    ans += i_ans // 2
 
print(ans)