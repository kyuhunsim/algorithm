a=int(input())

for i in range(a):

  m,n=map(int,input().split())

  queue=list(map(int,input().split()))  
  count=0
  idx=[j for j in range(m)]

  while queue:

    if queue[0]==max(queue):
      count+=1
      if idx[0]==n:
        print(count)
        break
      queue.pop(0)
      idx.pop(0)
        

    else:
      queue.append(queue.pop(0))
      idx.append(idx.pop(0))
      
      
    #안녕