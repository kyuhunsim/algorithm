import sys

N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

exchanges = 0
ans = -1

for last in range(N-1, 0, -1):
    max_index = 0
    for i in range(1, last+1):
        if A[i] > A[max_index]:
            max_index = i

    if last != max_index:
        exchanges += 1
        A[last], A[max_index] = A[max_index], A[last]

        if exchanges == K:
            print(*A)
if exchanges <K:
    print(-1)
