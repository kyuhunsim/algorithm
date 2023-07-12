# import sys
# N=int(sys.stdin.readline())
# A=list(map(int,sys.stdin.readline().split()))


# def selection_sort_distance(arr):
#     n=N
#     distance = {num: 0 for num in arr}
#     for i in range(n - 1):
#         min_idx = i
#         for j in range(i + 1, n):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
#         distance[arr[i]] += min_idx-i
#         distance[arr[min_idx]]+=min_idx-i  

#     return distance

# distance = selection_sort_distance(A)

# distance=dict(sorted(distance.items()))

# for value in distance.values():
#     print(value, end= ' ')

# N = int(input())
# A = list(map(int, input().split()))

# distance = [0] * N

# for i in range(N - 1):
#     min_idx = i
#     for j in range(i + 1, N):
#         if A[j] < A[min_idx]:
#             min_idx = j
    
#     A[i], A[min_idx] = A[min_idx], A[i]
    
#     distance[A[i] - 1] += min_idx - i
#     distance[A[min_idx] - 1] += min_idx - i

# print(*distance)

n = int(input())
nums = [0] + list(map(int, input().split()))
idx = [0 for _ in range(n+1)]
for i in range(1,n+1):
    idx[nums[i]] = i

ans = [0 for _ in range(n+1)]


for i in range(1,n+1):
    target = idx[i]

    ans[i] += target - i
    ans[nums[i]] += target - i

    nums[i], nums[target] = nums[target], nums[i]
    
    idx[nums[target]] = target
    idx[i] = i

print(*ans[1:])