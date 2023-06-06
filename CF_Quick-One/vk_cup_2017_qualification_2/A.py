import string

letters=string.ascii_lowercase

n,k=list(map(int,input().split(' ')))

for i in range(n):
	coordinate=i%k
	print(letters[coordinate], end="")
print()