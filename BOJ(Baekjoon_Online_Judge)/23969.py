import sys

N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))


exchanges = 0
ans = -1

for i in range(N-1, 0, -1):
	for j in range(i):
		if A[j] > A[j+1]:
			exchanges += 1
			A[j], A[j+1] = A[j+1], A[j]

			if exchanges == K:
				print(*A)
if exchanges < K:
	print(-1)
		
