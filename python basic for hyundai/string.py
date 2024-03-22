import sys
n=int(input())
ls=[]
for i in range(n):
    s,t=input().split()
    print(t[s.index('x')])
    ls.append(t[s.index('x')])

print(''.join(ls))
