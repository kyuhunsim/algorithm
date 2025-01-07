import math

n=int(input())

size=list(map(int,input().split()))

T,P=map(int,input().split())

cnt=0

cnt = sum(math.ceil(i / T) for i in size)

# 펜 최대 묶음 수 및 남은 개수 계산
print(cnt)
print(n // P, n % P)


# if문 썼던거는 반례 존재
# 1
# 0 0 0 0 0 1
# 2 2
    