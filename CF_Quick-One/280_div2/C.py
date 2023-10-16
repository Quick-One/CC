from sys import stdin
def input(): return stdin.readline()[:-1]

N, MAX, AVG = map(int, input().split())
ans = 0
tot = AVG * N
exams = []
for _ in range(N):
    a, b = map(int, input().split())
    tot -= a
    exams.append((b, a))

if tot <= 0:
    print(0)
    exit()

exams.sort()
for b, a in exams:
    can_be_done = MAX - a
    freq = min(can_be_done, tot)
    ans += freq * b
    tot -= freq
print(ans)