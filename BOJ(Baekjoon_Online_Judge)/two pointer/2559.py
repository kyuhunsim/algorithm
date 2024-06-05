import sys
input = sys.stdin.readline

n,k=map(int,input().split())

ls=list(map(int,input().split()))

# start=0
# end=k
# s=0
# st=[]

# for i in range(n):
#     # print(start+i,end+i)
#     s=sum(ls[start+i:end+i])
#     st.append(s)

# print(max(st))
# my first code
#-----------------------------

current_sum=sum(ls[:k])
max_sum=current_sum

for i in range(k,n):
    current_sum+=ls[i]-ls[i-k]
    if current_sum > max_sum:
        max_sum=current_sum

print(max_sum)