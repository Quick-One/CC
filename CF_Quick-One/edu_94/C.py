def stringslicing(string,index):
	if index>=0 and index<len(string):
		return string[index]
	else:
		return "not defined"

t=int(input())
for _ in range(t):
	string=input().strip()
	s=int(input())
	answer={}
	answer=answer.fromkeys(range(0,len(string)),"1")
	
	
	for i in range(len(string)):
		if string[i]=="0":
			a=i-s
			b=i+s
			if a>=0 and a<len(string):
				answer[a]="0"
			if b>=0 and b<len(string):
				answer[b]="0"
	
	ans="".join(answer.values())

	wrong=0
	for k in range(len(string)):
		if string[k]=="1":
			if string[k]==stringslicing(ans,k+s) or string[k]==stringslicing(ans, k-s):
				continue
			else:
				print(-1)
				wrong=1
				break

	if wrong==0:
		print(ans)

	