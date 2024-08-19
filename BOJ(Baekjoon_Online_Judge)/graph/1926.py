from collections import deque

n, m = map(int, input().split())
ls = [list(map(int, input().split())) for _ in range(n)]

# 방향 벡터 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start_x, start_y, visited):
    queue = deque()
    queue.append((start_x, start_y))
    visited[start_x][start_y] = True
    empty_space = 0

    while queue:
        x, y = queue.popleft()
        
        if ls[x][y] == 1:
            empty_space += 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and ls[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny))

    return empty_space

visited = [[False] * m for _ in range(n)]
empty_spaces_sizes = []

for i in range(n):
    for j in range(m):
        if ls[i][j] == 1 and not visited[i][j]:
            space_size = bfs(i, j, visited)
            empty_spaces_sizes.append(space_size)




if empty_spaces_sizes:
    print(len(empty_spaces_sizes))
    print(max(empty_spaces_sizes))
else:
    print(len(empty_spaces_sizes))
    print(0)