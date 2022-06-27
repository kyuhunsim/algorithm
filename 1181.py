a=int(input())

list=[]

for i in range(a):
    list.append(input())



list.sort(key=len)

print(list)