import math

def custom_round(n):
    return math.floor(n + 0.5)

n = int(input())

a= []

for i in range(n):
    a.append(int(input()))

a.sort()

cut = custom_round(n*0.15)

ls = a[cut:n-cut]


if n==0:
    print(0)
else:
    print(custom_round(sum(ls)/len(ls)))