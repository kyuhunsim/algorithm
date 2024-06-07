import sys
input=sys.stdin.readline
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def merge_sorted_arrays(N, A, M, B):
    i, j = 0, 0
    result = []
    
    # Merge the arrays using two pointers
    while i < N and j < M:
        if A[i] <= B[j]:
            result.append(A[i])
            i += 1
        else:
            result.append(B[j])
            j += 1
    
    # Append any remaining elements from A
    while i < N:
        result.append(A[i])
        i += 1
    
    # Append any remaining elements from B
    while j < M:
        result.append(B[j])
        j += 1
    
    return result

# Merging the arrays
sorted_array = merge_sorted_arrays(N, A, M, B)

# Output the result
print(' '.join(map(str, sorted_array)))