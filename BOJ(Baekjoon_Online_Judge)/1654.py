K, N= map(int,input().split())
ls=[]
for i in range(K):
    ls.append(int(input()))

def binary_search(array):
    min=1
    end=max(ls)
    
    while min <=end:
        mid=(min+end)//2
        lane=0
        for i in ls:
            lane+=i//mid
        
        if lane >= N:
            min=mid+1
        
        else:
            end=mid-1

    return end

print(binary_search(ls))