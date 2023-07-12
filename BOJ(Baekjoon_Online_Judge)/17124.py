def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return right


def find_closest_value(A, B):
    B.sort()  # Sort array B in ascending order
    
    C = []
    for num in A:
        # Use binary search to find the index of the closest value in B
        index = binary_search(B, num)
        
        # Check if the index is within the bounds of the array
        if index < 0:
            closest = B[0]
        elif index >= len(B) - 1:
            closest = B[-1]
        else:
            # Compare the values at the found index and the next index
            diff1 = abs(num - B[index])
            diff2 = abs(num - B[index + 1])
            if diff1 <= diff2:
                closest = B[index]
            else:
                closest = B[index + 1]
        
        C.append(closest)
    
    return C


# Read the number of test cases
T = int(input())

# Iterate over the test cases
for _ in range(T):
    # Read the values of n and m
    n, m = map(int, input().split())
    
    # Read array A
    A = list(map(int, input().split()))
    
    # Read array B
    B = list(map(int, input().split()))
    
    # Find array C
    C = find_closest_value(A, B)
    
    # Calculate and print the sum of elements in array C
    print(sum(C))
