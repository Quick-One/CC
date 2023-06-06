t=int(input())
for _ in range(t):
	n=int(input())
	string=input()
	answer=""
	for i in range(0,2*n-1,2):
		answer+=string[i]
	print(answer)