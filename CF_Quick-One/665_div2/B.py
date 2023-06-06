for _ in range(int(input())):
	ans=0
	a=list(map(int,input().strip().split(' ')))
	b=list(map(int,input().strip().split(' ')))

	twomax=min(a[2],b[1])
	ans+=2*twomax

	a[2]-=twomax
	b[1]-=twomax

	twominimise=min(a[0],b[2])
	a[0]-=twominimise
	b[2]-=twominimise
	
	twokill=min(a[2],b[2])
	a[2]-=twokill
	b[2]-=twokill

	ans-=min(b[2],a[1])*2
	print(ans)


