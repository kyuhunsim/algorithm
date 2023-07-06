def binary_search(array,search_value):
    lower_bound=0
    upper_bound=len(array)-1

    while lower_bound < upper_bound:
        midpoint = int((upper_bound+lower_bound)/2)
    
        value_at_midpoint = array[midpoint]

        if search_value == value_at_midpoint:
            return midpoint
        # 찾고자 하는 값이 중간 index보다 작을 때, midpoint보다 오른쪽을 모두 삭제
        # 따라서 upper bound를 midpoin-1로 바꿈
        elif search_value < value_at_midpoint:
            upper_bound=midpoint-1
        elif search_value > value_at_midpoint:
            lower_bound = midpoint +1
    
    return "there are no search_value in given array"

print(binary_search([3 , 17, 75 , 80 , 202] , 22))
