import sys
input=sys.stdin.readline
n,m=map(int,input().split())

ls=list(map(int,input().split()))

end=0
sum=0
cnt=0
for start in range(n):
    while sum <m and end <n:
        sum+=ls[end]
        end+=1
    
    if sum == m:
        cnt+=1
    sum-=ls[start]

print(cnt)