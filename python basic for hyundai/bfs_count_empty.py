from collections import deque

def count_enclosed_spaces(grid):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    
    def bfs(x, y):
        queue = deque([(x, y)])
        visited.add((x, y))
        is_enclosed = True  # 이 공간이 벽으로 둘러싸여 있는지 확인
        
        while queue:
            cx, cy = queue.popleft()
            
            # 만약 가장자리에 닿아 있는 공간이라면 이 공간은 외부와 연결됨
            if cx == 0 or cx == rows - 1 or cy == 0 or cy == cols - 1:
                is_enclosed = False
            
            # 상하좌우 방향 탐색
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy + dy
                
                # 유효한 범위 내, 빈 공간이며 방문하지 않은 칸
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0 and (nx, ny) not in visited:
                    queue.append((nx, ny))
                    visited.add((nx, ny))
        
        return is_enclosed
    
    enclosed_space_count = 0
    
    for i in range(rows):
        for j in range(cols):
            # 아직 방문하지 않은 빈 공간일 때만 탐색
            if grid[i][j] == 0 and (i, j) not in visited:
                if bfs(i, j):
                    enclosed_space_count += 1
    
    return enclosed_space_count

# 그리드 예시
grid = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

# 벽으로 둘러싸인 빈 공간의 개수 계산
enclosed_spaces = count_enclosed_spaces(grid)
print("벽으로 둘러싸인 빈 공간의 개수:", enclosed_spaces)
