def search_index_position(arr, target):
    left , right = 0, len(arr) -1

    while left <=right:
        mid = (left + right) // 2

        if arr[mid] ==target:
            return mid
        elif arr[mid] < target:
            left +=1
        else:
            right -=1
    
    return left

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 5
print(search_index_position(arr, target))

# Example usage for finding the index position to insert a target value
arr = [1, 2, 4, 5, 6, 7, 8, 9]
target = 3
print(search_index_position(arr, target))