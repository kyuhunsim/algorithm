n,m=map(int,input().split())
ls=list(map(int,input().split()))
end=0
sum=0
len=[]
for start in range(n):
    while sum < m and end <n:
        sum += ls[end]
        end+=1
    
    if sum == m:
        len.append(end-start+1)
    
    sum -=ls[start]

print(min(len))