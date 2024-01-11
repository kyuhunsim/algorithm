x1,y1,x2,y2= map(int,input().split())
x3,y3,x4,y4= map(int,input().split())

def ccw(x1,y1,x2,y2,x3,y3):
    ans=(x1*y2+x2*y3+x3*y1)-(y1*x2+y2*x3+y3*x1)
    if ans>0:
        return 1
    elif ans<0:
        return -1
    else:
        return 0

def isOverlab(x1,y1,x2,y2,x3,y3,x4,y4):
    if ccw(x1,y1,x2,y2,x3,y3)*ccw(x1,y1,x2,y2,x4,y4)==0 and ccw(x3,y3,x4,y4,x1,y1)*ccw(x3,y3,x4,y4,x2,y2)==0:
        if x1>x2:
            x1,x2=x2,x1
        if y1>y2:
            y1,y2=y2,y1
        if x3>x4:
            x3,x4=x4,x3
        if y3>y4:
            y3,y4=y4,y3
        if x1<=x4 and x3<=x2 and y1<=y4 and y3<=y2:
            return 1
        else:
            return 0
    elif ccw(x1,y1,x2,y2,x3,y3)*ccw(x1,y1,x2,y2,x4,y4)<=0 and ccw(x3,y3,x4,y4,x1,y1)*ccw(x3,y3,x4,y4,x2,y2)<=0:
        return 1
    else:
        return 0

print(isOverlab(x1,y1,x2,y2,x3,y3,x4,y4))
