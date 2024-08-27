T=int(input())

for i in range(T):
    
    ls=list(input().split())
    a=float(ls[0])

    for i in range(1,len(ls)):
        if ls[i]== '@':
            a=3*a

        elif ls[i]=='%':
            a+=5

        else:
            a=a-7
            

    print("{:.2f}".format(a))