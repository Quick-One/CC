for _ in range(int(input())):
	ans=0
	n,k=map(int,input().split(' '))
	if k>=n:
		ans+=k-n
	else:
		if k%2==n%2:
			ans=0
		else:
			ans=1

	print(ans)
