from sys import stdin, stdout
from math import ceil
def Integer(): return int(stdin.readline().strip())
def MapInteger(): return map(int, stdin.readline().strip().split())
def MapList(): return list(map(int, stdin.readline().split()))
from collections import defaultdict
dic=defaultdict(int)
n=Integer()
Data=MapList()
for i in Data:
	dic[i]+=1

answer=0
answer+=dic[4]
answer+=dic[3]
dic[1]-=min(dic[1],dic[3])

answer+=dic[2]//2
dic[2]-=(dic[2]//2)*2
dummy=dic[2]*2+dic[1]
answer+=ceil(dummy/4)
print(answer)