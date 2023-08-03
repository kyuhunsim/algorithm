N,M=map(int,input().split())
ls=[]
for i in range(N):
    ls.append(int(input()))


def binary_search(array,M):
    min=0
    end=max(array)*M

    while min <=end:
        mid=(min+end)//2
        cnt=0
        for i in ls:
            cnt+=mid//i
        print('mid',mid)
        print('cnt',cnt)
        
        if cnt < M:
            min=mid+1
        else:
            end=mid-1
    return end

print(binary_search(ls,M)+1)



