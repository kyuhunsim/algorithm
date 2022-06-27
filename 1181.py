a=int(input())

list=[]

for i in range(a):
    list.append(int(input()))



list.sort(key=len)

print(list)