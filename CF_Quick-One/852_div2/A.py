from sys import stdin
import sys
def input(): return stdin.readline()[:-1]
anses = []
for _ in range(int(input())):
    a,b = map(int,input().split())
    n,m = map(int,input().split())
    q,r = divmod(n, m+1)
    ans = q * min(a*m, b*(m+1)) + r * min(a, b)
    anses.append(ans)
sys.stdout.write('\n'.join(map(str,anses)))