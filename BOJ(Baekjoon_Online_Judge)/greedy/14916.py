import sys
input=sys.stdin.readline

def min_coins(n):
    # 5원짜리 동전의 개수를 줄여가며 확인
    for i in range(n // 5, -1, -1):  # n // 5부터 0까지 감소하며 반복
        remainder = n - i * 5  # 5원 동전을 i개 사용했을 때 남은 금액
        if remainder % 2 == 0:  # 남은 금액이 2로 나누어 떨어지면
            return i + remainder // 2  # 5원 동전 개수 + 2원 동전 개수
    return -1  # 거슬러 줄 수 없으면 -1

# 입력 받기
n = int(input().strip())
# 결과 출력
print(min_coins(n))