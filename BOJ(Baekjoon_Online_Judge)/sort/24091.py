import sys
sys.setrecursionlimit(10**5)

def quick_sort(A, p, r, K, swap_count):
    if swap_count[0] >= K or p >= r:
        return
    q = partition(A, p, r, K, swap_count)
    quick_sort(A, p, q - 1, K, swap_count)
    quick_sort(A, q + 1, r, K, swap_count)

def partition(A, p, r, K, swap_count):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            if swap_count[0] < K:
                A[i], A[j] = A[j], A[i]  
                swap_count[0] += 1
    if i + 1 != r and swap_count[0] < K:
        A[i + 1], A[r] = A[r], A[i + 1]  
        swap_count[0] += 1
    return i + 1

A,K=map(int,input().split())
A_list=list(map(int,input().split()))

swap_count = [0]
quick_sort(A_list, 0, A- 1, K, swap_count)
if swap_count[0] < K:
    print(-1)
else:
    print(*A_list)
