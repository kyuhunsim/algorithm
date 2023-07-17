# 2512번 실버3 이분탐색 예산

N=int(input())
ls=list(map(int,input().split()))
M=int(input())

def binary_search(array,M):
    start=1
    end=max(array)

    while start <= end:
        mid=(start+end)//2
        budget=0
        for value in ls:
            if value >= mid:
                budget+=mid
            else:
                budget+=value
        if budget <=M:
            start=mid+1
        
        else:
            end=mid-1
    return end

print(binary_search(ls,M))