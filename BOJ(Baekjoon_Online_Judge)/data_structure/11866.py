from collections import deque

queue=deque()
ans=[]


a,b=map(int,input().split())

for i in range(1,a+1):
  queue.append(i)

while queue:
  for i in range(b-1):
    queue.append(queue.popleft())
    
  ans.append(queue.popleft())



print("<",end="")
for i in range(len(ans)-1):
  print("%d, "%ans[i],end="")

print(ans[-1],end="")
print(">")