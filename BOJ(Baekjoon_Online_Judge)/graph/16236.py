from collections import deque

n = int(input())

ls = []
for i in range(n):
    a = list(map(int, input().split()))
    ls.append(a)

# Find the initial position of the shark
shark_x, shark_y = None, None
for i in range(n):
    for j in range(n):
        if ls[i][j] == 9:
            shark_x, shark_y = i, j
            ls[i][j] = 0  # 아기 상어의 위치를 빈 칸으로 설정
            break
    if shark_x is not None:
        break

def bfs(start_x, start_y, size):
    queue = deque()
    visited = [[False] * n for _ in range(n)]
    queue.append((start_x, start_y, 0))
    visited[start_x][start_y] = True
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    fish_list = []
    while queue:
        x, y, dist = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = True
                if 0 < ls[nx][ny] < size:  # 먹을 수 있는 물고기
                    fish_list.append((dist + 1, nx, ny))
                elif ls[nx][ny] == 0 or ls[nx][ny] == size:  # 상어가 지나갈 수 있는 칸
                    queue.append((nx, ny, dist + 1))
    
    if fish_list:
        fish_list.sort()
        return fish_list[0]  # 가장 가까운 물고기 반환
    else:
        return None

size = 2
eat_cnt = 0
time = 0

while True:
    result = bfs(shark_x, shark_y, size)

    if result is None:  # 더 이상 먹을 수 있는 물고기가 없을 때
        break

    dist, new_x, new_y = result
    shark_x, shark_y = new_x, new_y
    time += dist
    ls[shark_x][shark_y] = 0
    eat_cnt += 1

    if eat_cnt == size:  # 아기 상어 크기 증가
        size += 1
        eat_cnt = 0

print(time)
