# 2805번 이진 탐색 실버2 나무자르기
import sys
N, M=map(int,input().split())
wood=list(map(int,sys.stdin.readline().split()))

def binary_search(array):
    min=1
    end=max(wood)
    while min <= end:
        mid=(min+end)//2
        cnt=0
        for i in wood:
            if i >= mid:
                cnt+=i-mid
        if cnt <M:
            end=mid-1
        else:
            min=mid+1

    return end

print(binary_search(wood))
