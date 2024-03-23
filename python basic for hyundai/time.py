min=0
for i in range(5):
    a,b=input().split()
    hour_0=int(a.split(':')[0])
    minute_0=int(a.split(':')[1])
    hour_1 = int(b.split(':')[0])
    minute_1 = int(b.split(':')[1])
    # if  minute_0 > minute_1:
    #    min += (hour_1-hour_0)*60+(minute_0-minute_1)
    # else:
    min +=(hour_1-hour_0)*60+(minute_0-minute_1)

print(min)