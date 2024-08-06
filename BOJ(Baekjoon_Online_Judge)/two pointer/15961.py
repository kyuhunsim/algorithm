import sys
input=sys.stdin.readline

n,d,k,c=map(int,input().split())
ls = [int(input().strip()) for _ in range(n)]

current = ls[:k]
sushi_counter={}

for sushi in current:
    if sushi in sushi_counter:
        sushi_counter[sushi]+=1
    else:
        sushi_counter[sushi] = 1


# max=len(set(current))+(1 if c not in current else 0)

# set_current=set(current)

# for i in range(1,n):
#     set_current.remove(ls[i-1])
#     set_current.add(ls[(i+k-1)%n])
#     unique=len(set_current)

#     if c not in set_current:
#         unique+=1

#     if unique > max:
#         max= unique

# print(max)

print(current)
print(sushi_counter)

