# To find the value in array linearly
# SO, the speed of search would be slow

def linear_search(array,search_value):
    
    for index in range(len(array)):
        if search_value ==array[index]:
            return print("Search_value is at index", index)  
        return "Search_value is not in given array"

array=[3,17,75,80,22]
search_value=75

print(linear_search(array,search_value))