x = 0
t = int(input())
for _ in range(t):
	s = input()
	if '-' in s :
		x-= 1
	else:
		x += 1

print(x)