for _ in range(int(input())):
	ans=0
	n,m=map(int,input().strip().split(' '))
	for i in range(n-1):
		if input()[-1]=="R":
			ans+=1
	ans+=input().count('D')
	print(ans) 