N=int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ls=[]
for i in range(1,N):
    loc=i-1
    new=A[i]

    while (loc>=0 and new <A[loc]):
        A[loc+1]=A[loc]
        loc-=1
        if A==B:
            ls.append(1)

    if loc+1!=i:
        A[loc+1]=new
        if A==B:
            ls.append(1)

if len(ls)==1:
    print(1)
else:
    print(0)

