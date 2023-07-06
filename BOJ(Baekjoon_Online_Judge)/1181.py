a=int(input())

list_2=[]

for i in range(a):
    list_2.append(input())
set_list=set(list_2)
list_2=list(set_list)
list_2.sort()
list_2.sort(key=len)

for i in list_2:
    print(i)