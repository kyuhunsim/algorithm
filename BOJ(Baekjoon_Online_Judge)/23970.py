def bubble_sort(A, B, n):

    # 1 if A and B are the same from the beginning
    if A == B:
        return 1

    # last, last2: Indexes that have been sorted do not need to run for statements
    last = n - 1
    last2 = 0
    for i in range(n - 1):
        if last == 0:
            break
        check = 0
        for j in range(last):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                check += 1
                last2 = j

                # without having to compare all elements each time the sort is performed
                # Check the A and B arrays by checking only the changed elements
                if A[j] == B[j]:
                    if A == B:
                        return 1
        last = last2
        # break if nothing changes;
        if check == 0:
            break

    return 0

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(bubble_sort(A, B, n))

