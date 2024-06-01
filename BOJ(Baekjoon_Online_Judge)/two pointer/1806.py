import sys
input=sys.stdin.readline
n,s=map(int,input().split())
ls=list(map(int,input().split()))
end=0
sum=0
length=[]

for start in range(n):
    while sum < s and end <n:
        sum += ls[end]
        end+=1
    
    if sum >= s:
        length.append(end-start)
    
    sum -=ls[start]

if len(length)==0:
    print(0)
else:
    print(min(length))