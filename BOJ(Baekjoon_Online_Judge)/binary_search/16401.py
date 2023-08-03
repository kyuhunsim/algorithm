M,N=map(int,input().split())
ls=list(map(int,input().split()))
def binary_search(array):
    min=1
    end=max(ls)
    
    while min <=end:
        cnt=0
        mid=(min+end)//2
        for cookie in ls:
            cnt+=cookie//mid
        
        if cnt >=M:
            min=mid+1
        else:
            end=mid-1
    
    return end

print(binary_search(ls))
        