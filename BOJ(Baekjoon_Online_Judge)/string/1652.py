def count_lie_down_places(N, room):
    horizontal_count = 0
    vertical_count = 0
    
    # 가로 방향 검사
    for row in room:
        count = 0
        for char in row:
            if char == '.':
                count += 1
            else:
                if count >= 2:
                    horizontal_count += 1
                count = 0
        if count >= 2:
            horizontal_count += 1
    
    # 세로 방향 검사
    for col in range(N):
        count = 0
        for row in range(N):
            if room[row][col] == '.':
                count += 1
            else:
                if count >= 2:
                    vertical_count += 1
                count = 0
        if count >= 2:
            vertical_count += 1
    
    return horizontal_count, vertical_count

# 입력 받기
N = int(input())
room = [input().strip() for _ in range(N)]

# 결과 계산
horizontal_count, vertical_count = count_lie_down_places(N, room)

# 결과 출력
print(horizontal_count, vertical_count)
