import sys
input=sys.stdin.readline

w,n=map(int,input().split())
ls=[]
for i in range(n):
    m,p=map(int,input().split())
    ls.append((m,p))

value=0
ls.sort(key=lambda x: x[1], reverse=True)

for m,p in ls:
    if m <= w:
        value+= m*p
        w-=m
    else:
        value += w*p
        break

print(value)