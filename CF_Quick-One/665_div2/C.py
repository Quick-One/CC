for _ in range(int(input())):
	n=input()
	lis=list(map(int,input().strip().split()))
	sortedlist=sorted(lis)
	ans="YES"
	least=min(lis)
	if least==1:
		print(ans)
	else:
		for i in range(len(lis)):
			if lis[i]%least==0:
				continue
			else:
				if lis[i]!=sortedlist[i]:
					ans="NO"
				else:
					continue
		print(ans)
