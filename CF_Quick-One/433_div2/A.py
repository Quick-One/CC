import math

n=int(input())
if n%2==1:
	a,b=n//2,n//2+1
else:
	a,b=n//2-1, n//2+1

while math.gcd(a,b)!=1:
	a-=1
	b+=1

print(a,b) 