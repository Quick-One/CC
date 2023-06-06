modulo=10**9+7
factorial=1
twopower=1
n=int(input())


for i in range(n-1):
	twopower=(twopower*2)%modulo

for i in range(1,n+1):
	factorial=(factorial*i)%modulo

print((factorial-twopower)%modulo)