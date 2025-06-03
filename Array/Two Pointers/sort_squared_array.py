"""
You are given a sorted array of integers (can include negative numbers).
Return a new array containing the squares of each number, sorted in non-decreasing order."""

def sorted_squared_array(array):
    n = len(array)
    result = [0] * n
    left = 0
    right = n -1
    pos = n - 1

    while left <=right:
        if abs(array[left]) > abs(array[right]):
            result[pos] = array[left] ** 2
            left +=1
        else:
            result[pos] = array[right] ** 2
            right -=1
        pos -= 1
    return result


# Example usage:
array = [-4, -2, 0, 3, 5]
print(sorted_squared_array(array))  