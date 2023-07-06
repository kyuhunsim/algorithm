a=int(input())
list=[]
for i in str(a):
  list.append(i)


list.sort(reverse=True)

for j in list:
  print(j,end="")