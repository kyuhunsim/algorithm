from collections import deque

n,m=map(int,input().split())

ls=[]
for i in range(m):
    ls.append(list(map(int,input().split())))

def multi_bfs():
    queue=deque()
    visited=[[False]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if ls[i][j] == 1:
                queue.append((i, j,0))
                visited[i][j] = True
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    max_dist=0
    while queue:
        x,y,dist=queue.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and ls[nx][ny]==0:
                
                visited[nx][ny] = True
                queue.append((nx,ny,dist+1))
                max_dist=max(max_dist,dist+1)
                
    for i in range(m):
        for j in range(n):
            if ls[i][j] == 0 and not visited[i][j]:
                return -1  # 모든 0을 채울 수 없는 경우 -1 반환

    return max_dist

print(multi_bfs())