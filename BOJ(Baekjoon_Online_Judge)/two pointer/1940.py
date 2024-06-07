import sys
input = sys.stdin.readline

n=int(input())
m=int(input())

num=list(map(int,input().split()))

start=0
end=len(num)-1
cnt=0
num.sort()

while start < end:

    if num[start] + num[end] == m:
        cnt+=1 
        start+=1
        end-=1
    elif num[start] + num[end] < m:
        start+=1
    else:
        end-=1

print(cnt)