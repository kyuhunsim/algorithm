import sys
input=sys.stdin.readline
n=int(input())
ls=list(map(int,input().split()))
x=int(input())

end=1
cnt=0
sum=0

def count_pairs(arr, x):
    arr.sort()  # 정렬
    left = 0
    right = len(arr) - 1
    count = 0
    
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == x:
            count += 1
            left += 1
            right -= 1
        elif current_sum < x:
            left += 1
        else:
            right -= 1
    
    return count

print(count_pairs(ls,x))