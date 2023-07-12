# 1838 골드 1 버블정렬 문제 X, 그냥 정렬 이해에 대한 문제

N=int(input())
A=list(map(int,input().split()))
sorted_list=sorted(A)

def calculate_element_distances(regular_list, sorted_list):
    index_mapping = {}
    distances = []

    for index, value in enumerate(sorted_list):
        if value not in index_mapping:
            index_mapping[value] = []

        index_mapping[value].append(index)
        
    for index, element in enumerate(regular_list):
        sorted_indices = index_mapping[element]
        distance = min(abs(sorted_index - index) for sorted_index in sorted_indices)
        distances.append(distance)

    return max(distances)

print(calculate_element_distances(A, sorted_list))
