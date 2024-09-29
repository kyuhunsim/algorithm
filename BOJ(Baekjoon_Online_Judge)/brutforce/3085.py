n = int(input())

ls = []
for i in range(n):
    candy = list(input())
    ls.append(candy)

def check_max(ls):
    max_count = 1
    
    # 가로로 연속된 사탕 개수 체크
    for i in range(n):
        count = 1
        for j in range(1, n):
            if ls[i][j] == ls[i][j-1]:
                count += 1
            else:
                count = 1
            max_count = max(max_count, count)

    # 세로로 연속된 사탕 개수 체크
    for i in range(n):
        count = 1
        for j in range(1, n):
            if ls[j][i] == ls[j-1][i]:
                count += 1
            else:
                count = 1
            max_count = max(max_count, count)
    
    return max_count

max_candies = 1

# 가로로 인접한 두 칸 교환
for i in range(n):
    for j in range(n-1):
        # 교환
        ls[i][j], ls[i][j+1] = ls[i][j+1], ls[i][j]
        # 최대값 확인
        max_candies = max(max_candies, check_max(ls))
        # 원상 복구
        ls[i][j], ls[i][j+1] = ls[i][j+1], ls[i][j]

# 세로로 인접한 두 칸 교환
for i in range(n-1):
    for j in range(n):
        # 교환
        ls[i][j], ls[i+1][j] = ls[i+1][j], ls[i][j]
        # 최대값 확인
        max_candies = max(max_candies, check_max(ls))
        # 원상 복구
        ls[i][j], ls[i+1][j] = ls[i+1][j], ls[i][j]

print(max_candies)
