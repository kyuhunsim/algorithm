## 1920번 이분탐색 실버4
import sys
N=int(input())
A=list(map(int,sys.stdin.readline().split()))
M=int(input())
B=list(map(int,sys.stdin.readline().split()))
A.sort()

def binary_search(array,search_value):
    low=0
    high=len(array)-1
    while low<=high:
        midpoint=int((low+high)/2)

        if search_value==array[midpoint]:
            return 1
        elif search_value < array[midpoint]:
            high=midpoint-1
        elif search_value > array[midpoint]:
            low=midpoint+1

    return 0

for value in B:
    print(binary_search(A,value))
