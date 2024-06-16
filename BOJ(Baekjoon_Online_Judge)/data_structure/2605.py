a=int(input())

ls=list(map(int,input().split()))
zero=[]

for i in range(a):
  zero.insert(ls[i],i+1)
  

for i in range(len(zero)):
  print(zero[-i-1],end=" ")



