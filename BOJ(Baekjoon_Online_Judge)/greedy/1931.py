import sys
input=sys.stdin.readline


n=int(input())

cnt=0
end_time=0

ls=[]

for i in range(n):
    s,e=map(int,input().split())
    ls.append((s,e))


ls.sort(key=lambda x:(x[1],x[0]))

for start, end in ls:
    if start >=end_time:
        cnt+=1
        end_time=end

print(cnt)