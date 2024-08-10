# graph = {
#     'A': ['B', 'C'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F'],
#     'D': ['B'],
#     'E': ['B', 'F'],
#     'F': ['C', 'E']
# }

# def dfs_stack(graph, start):
#     visited = set()
#     stack = [start]

#     while stack:
#         node = stack.pop()
#         if node not in visited:
#             print(node, end=" ")
#             visited.add(node)
#             stack.extend(reversed(graph[node]))  # 스택에 이웃 노드들을 추가

# # DFS 실행
# dfs_stack(graph, 'A')

grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

from collections import deque

def bfs_grid(grid, start_x, start_y):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    queue = deque([(start_x, start_y)])
    visited.add((start_x, start_y))

    while queue:
        x, y = queue.popleft()
        print(f"Visiting ({x}, {y})")

        # 상하좌우 방향 탐색
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            # 그리드 범위 내에 있고, 방문하지 않았으며 벽이 아닌 경우
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and grid[nx][ny] == 0:
                queue.append((nx, ny))
                visited.add((nx, ny))

# BFS 실행 (시작점은 (0, 0))
bfs_grid(grid, 0, 0)