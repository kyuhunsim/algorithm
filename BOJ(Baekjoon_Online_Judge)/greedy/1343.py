def cover_board(board):
    # '.'으로 나누어 X로 이루어진 덩어리들을 얻음
    parts = board.split('.')
    
    result = []
    
    for part in parts:
        if not part:  # 빈 문자열은 무시 (중간의 '.'은 고려하지 않음)
            result.append('')
            continue
        
        # 'AAAA'로 최대한 채우고 남은 부분을 'BB'로 채움
        n = len(part)
        if n % 2 == 1:  # X의 길이가 홀수면 덮을 수 없음
            return '-1'
        
        # 'AAAA'로 최대한 채우기
        result.append('AAAA' * (n // 4))
        
        # 나머지를 'BB'로 채우기
        n = n % 4
        if n == 2:
            result[-1] += 'BB'  # 기존에 추가된 문자열에 이어 붙이기
    
    # 각 부분을 '.'을 기준으로 다시 합침
    return '.'.join(result)

# 입력 받기
board = input().strip()
# 결과 출력
print(cover_board(board))
