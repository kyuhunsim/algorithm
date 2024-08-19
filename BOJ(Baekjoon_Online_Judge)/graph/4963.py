from collections import deque

def bfs (start_x,start_y,visited):
    queue=deque()
    queue.append((start_x,start_y))
    visited[start_x][start_y]=True
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]
    area=1
    while queue:
        x,y=queue.popleft()

        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]

            while 0<= nx < h and 0 <= ny <w  and not visited[nx][ny] and ls[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny))



    return area

while True:
    cnt=0
    w,h=map(int,input().split())
    if w ==0 and h ==0:
        break
    ls=[list(map(int,input().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if ls[i][j] == 1 and not visited[i][j]:
                cnt += 1
                bfs(i,j,visited)
    
    print(cnt)

    



    

