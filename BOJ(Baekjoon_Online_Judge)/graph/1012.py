from collections import deque

T=int(input())


def bfs(grid,x,y):
    rows=N
    cols=M
    queue=deque([(x,y)])
    visited.add((x,y))

    while queue:
        cx,cy=queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy        
            # 유효한 범위 내, 빈 공간이며 방문하지 않은 칸
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1 and (nx, ny) not in visited:                    
                queue.append((nx, ny))
                visited.add((nx, ny))

for i in range(T):
    M,N,K=map(int,input().split())
    grid=[[0]*M for _ in range(N)]
    visited=set()
    for i in range(K):
        x,y= map(int,input().split())
        grid[y][x] = 1
    enclosed_space_count=0
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1 and (i, j) not in visited:
                bfs(grid,i, j)
                enclosed_space_count += 1
                
    print(enclosed_space_count)

