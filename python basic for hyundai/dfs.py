n,m=map(int,input().split())
ls=[]
for i in range(n):
    ls.append(list(map(int,input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

from collections import deque

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x +dx[i]
            ny = y + dy[i]
        
        if nx < 0 or nx>=n or ny< 0 or ny>=m:
            continue
        
        if ls[nx][ny]==0:
            continue
        if ls[nx][ny]==1:
            ls[nx][ny]=ls[nx][ny]+1
            queue.append((nx,ny))
        
        return ls[n-1][m-1]

print(bfs(0,0))

