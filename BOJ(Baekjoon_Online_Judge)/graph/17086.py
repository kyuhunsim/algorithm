from collections import deque

n, m = map(int, input().split())

ls = []
for _ in range(n):
    ls.append(list(map(int, input().split())))

def multi_bfs():
    queue = deque()
    visited = [[-1] * m for _ in range(n)]
    
    # 모든 아기 상어 위치를 큐에 추가하고 방문 처리
    for i in range(n):
        for j in range(m):
            if ls[i][j] == 1:
                queue.append((i, j))
                visited[i][j] = 0  # 아기 상어 위치의 거리는 0으로 설정

    # 8방향 (상하좌우 및 대각선)
    dx = [-1, 1, 0, 0, -1, -1, 1, 1]
    dy = [0, 0, -1, 1, -1, 1, -1, 1]

    # BFS 수행
    while queue:
        x, y = queue.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
    
    # 빈 칸 중 최대 거리 계산
    max_distance = 0
    for i in range(n):
        for j in range(m):
            if ls[i][j] == 0:
                max_distance = max(max_distance, visited[i][j])
    
    return max_distance

# 결과 출력
result = multi_bfs()
print(result)
