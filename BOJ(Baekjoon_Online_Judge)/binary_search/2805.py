# 2805번 이진 탐색 실버2 나무자르기
import sys
N, M = map(int, input().split())
wood = list(map(int, sys.stdin.readline().split()))

def binary_search(array):
    min = 0
    end = max(wood)
    while min <= end:
        mid = (min + end) // 2
        cnt = 0
        
        # 잘린 나무의 길이를 계산하여 M과 비교
        for i in wood:
            if i >= mid:
                cnt += i - mid
        
        # 잘린 나무의 길이가 M보다 작으면 mid를 감소시켜야 함
        if cnt < M:
            end = mid - 1

        # 잘린 나무의 길이가 M보다 크거나 같으면 mid를 증가시켜야 함
        else:
            min = mid + 1

    return end

print(binary_search(wood))
