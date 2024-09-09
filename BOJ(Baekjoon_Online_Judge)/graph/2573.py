from collections import deque

# 상하좌우 이동을 위한 좌표
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS로 연결된 빙산 탐색
def bfs(x, y, visited, iceberg, n, m):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and iceberg[nx][ny] > 0:
                visited[nx][ny] = True
                queue.append((nx, ny))

# 빙산 녹이기 함수
def melt_iceberg(iceberg, n, m):
    melted = [[0] * m for _ in range(n)]  # 녹는 양을 기록
    
    for i in range(n):
        for j in range(m):
            if iceberg[i][j] > 0:
                water_count = 0  # 주변 바다(0)의 개수
                for k in range(4):
                    ni = i + dx[k]
                    nj = j + dy[k]
                    if 0 <= ni < n and 0 <= nj < m and iceberg[ni][nj] == 0:
                        water_count += 1
                melted[i][j] = water_count
    
    for i in range(n):
        for j in range(m):
            iceberg[i][j] = max(0, iceberg[i][j] - melted[i][j])

# 빙산 덩어리 개수 계산
def count_iceberg_chunks(iceberg, n, m):
    visited = [[False] * m for _ in range(n)]
    chunk_count = 0
    
    for i in range(n):
        for j in range(m):
            if iceberg[i][j] > 0 and not visited[i][j]:
                bfs(i, j, visited, iceberg, n, m)
                chunk_count += 1
    
    return chunk_count

def simulate_iceberg(iceberg, n, m):
    year = 0
    
    while True:
        # 빙산 덩어리 개수 확인
        chunks = count_iceberg_chunks(iceberg, n, m)
        if chunks >= 2:
            return year
        if chunks == 0:
            return 0
        
        # 빙산을 녹임
        melt_iceberg(iceberg, n, m)
        
        # 연도 증가
        year += 1

# 입력 받기
n, m = map(int, input().split())
iceberg = [list(map(int, input().split())) for _ in range(n)]

# 시뮬레이션 실행
result = simulate_iceberg(iceberg, n, m)
print(result)
