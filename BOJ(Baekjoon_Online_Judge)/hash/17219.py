N,M=map(int,input().split())
dic={}
for i in range(N):
    add,pw=input().split()
    dic[add]=pw

for i in range(M):
    a=input()
    print(dic[a])
    