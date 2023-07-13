def selection_sort(array):
    for i in range(len(array)-1):
        lowest = i
        for j in range(i+1, len(array)):
            if array[j] < array[lowest]:
                lowest = j
        
        if lowest != i:
            array[i], array[lowest] = array[lowest], array[i]
    
    return array

print(selection_sort([3, 1, 2, 5, 4]))
