n=input()
lis=list(map(int,input().split(' ')))
least,highest=min(lis),max(lis)
print((highest-least+1)-len(lis))