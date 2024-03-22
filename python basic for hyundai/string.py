import sys
n=int(input())
ls=[]
for i in range(n):
    s,t=input().split()
    if 'x' in s:
        a=t[s.index('x')]
        a=a.upper()
        ls.append(a)
    else:
        
        ls.append(t[s.index('X')])

print(''.join(ls))