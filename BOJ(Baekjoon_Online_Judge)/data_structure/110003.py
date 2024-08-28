import sys
import heapq

size, length = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
res = []
H = []

for i in range(size):
    heapq.heappush(H, (A[i], i))
    
    # 범위를 벗어난 요소가 있을 경우 제거
    while H[0][1] <= i - length:
        print(H)
        heapq.heappop(H)8

    # 윈도우의 최소값 추가 (i가 length - 1보다 클 때부터)
    res.append(H[0][0])

for r in res:
    print(r, end=' ')
# import sys
# import heapq

# size, length = map(int, sys.stdin.readline().split())
# A = list(map(int, sys.stdin.readline().split()))
# res = []
# # Heap
# H = []

# for i in range(size):
#     heapq.heappush(H, (A[i], i))
#     if i < length:
#         res.append(H[0][0])   
#     else:
#         if H[0][1] <= i - length:
#             heapq.heappop(H)
#         res.append(H[0][0])    

# for r in res:
#     print(r, end = ' ')