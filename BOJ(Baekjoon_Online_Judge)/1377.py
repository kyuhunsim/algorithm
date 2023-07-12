N=int(input())
A=[]
for i in range(N):
    A.append((int(input()),i))

sorted_list=sorted(A)


cnt=[]
for i in range(N):
    cnt.append(sorted_list[i][1]-A[i][1])

print(max(cnt)+1)    