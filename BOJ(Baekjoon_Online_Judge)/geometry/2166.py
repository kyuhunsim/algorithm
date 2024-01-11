n=int(input())
x=[]
y=[]

for i in range(n):
    a,b=map(int,input().split())
    x.append(a)
    y.append(b)

x.append(x[0])
y.append(y[0])

def ccw(x,y):
    ans=0
    for i in range(n):
        ans+=(x[i]*y[i+1]-x[i+1]*y[i])
    return abs(ans)/2

print('%.1f'%ccw(x,y)) 
# 소숫점 둘째자리에서 반올림해서 첫째자리까지만 출력하는 방법
