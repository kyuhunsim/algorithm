from collections import deque

n=int(input())

def bfs(start_x,start_y,visited,goal_x,goal_y):
    queue=deque()
    queue.append((start_x,start_y,0))

    visited[start_x][start_y]=True
    dx = [-2, -1, 1, 2, 2, 1, -1, -2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]
    while queue:
        x,y,dist=queue.popleft()

        if x==goal_x and y==goal_y:
            return dist

        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<a and 0<=ny<a and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny,dist+1))

    return 0

for i in range(n):
    a=int(input())
    
    start_x,start_y=map(int,input().split())
    goal_x,goal_y=map(int,input().split())
    visited=[[False]*a for _ in range(a)]
    b=bfs(start_x,start_y,visited,goal_x,goal_y)
    print(b)