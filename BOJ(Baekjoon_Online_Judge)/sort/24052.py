N,K = map(int,input().split())
A = list(map(int, input().split()))

save=0
for i in range(1,N):
    loc=i-1
    new=A[i]

    while (loc>=0 and new <A[loc]):
        A[loc+1]=A[loc]
        loc-=1
        save+=1
        if save==K:
            for i in A:
                print(i,end=' ')

    if loc+1!=i:
        A[loc+1]=new
        save+=1
        if save==K:
            for i in A:
                print(i,end=' ')
    
if save<K:
    print(-1)

