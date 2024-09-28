import sys
input=sys.stdin.readline

n,m=map(int,input().split())
j=int(input())
ls=[]
for i in range(j):
    d=int(input())
    ls.append(d)

left=0
right=m
cnt=0

for i in ls:
    