import sys

## 백준 10815번 문제 실버 5 이진탐색 문제

N=int(input())
ls_1=list(map(int,sys.stdin.readline().split()))
M=int(input())
ls_2=list(map(int,sys.stdin.readline().split()))
ls_1=sorted(ls_1)

def binary_search(array,search_value):
    low=0
    high=len(array)-1
    
    while low<=high:
        midpoint=(int((low+high)/2))

        if search_value==array[midpoint]:
            return 1
        elif search_value > array[midpoint]:
            low=midpoint+1
        elif search_value <array[midpoint]:
            high=midpoint-1

    return 0

for value in ls_2:
    print(binary_search(ls_1,value),end=" ")