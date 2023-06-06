from sys import stdin, stdout
from collections import defaultdict, deque, Counter, OrderedDict


def Integer(): return int(stdin.readline().strip())
def MapInteger(): return map(int, stdin.readline().strip().split())
def MapList(): return list(map(int, stdin.readline().split()))

for _ in range(int(input())):
	k=int(input())
	array=list(MapInteger())

	countnum=Counter(array)


	first=True
	second=True
	a,b=0,0

	for i in range(max(array)+1):

		
		if countnum[i]>=2:
			if first:

				a+=1
			if second:

				b+=1
		
		if countnum[i]==1:

			if first:
				a+=1
			if second:
				second=False
		
		if countnum[i]==0:
			if first:
				first=False
			if second:
				second=False
	print(a+b)