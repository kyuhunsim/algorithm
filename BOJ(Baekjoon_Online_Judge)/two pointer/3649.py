import sys
input= sys.stdin.readline

while True:
    try:
        x=int(input())
        n=int(input())

        length=[]

        for i in range(n):
            length.append(int(input()))

        goal=x*10000000

        start=0
        end=n-1
        m=0
        cnt=0

        length.sort()

        tmp=True

        while start < end:
            current_sum = length[start] + length[end]
            if current_sum == goal:
                print('yes', length[start], length[end])
                tmp=False
                break
            elif current_sum < goal:
                start += 1
            else:
                end -= 1

        if tmp:
            print('danger')
    except:
        break