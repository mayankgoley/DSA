def find_peak_of_mountain(arr):
    left , right = 0, len(arr) -1

    while left < right:
        mid = (left + right) // 2

        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
    
    return left

# Example usage:
arr = [0, 2, 1, 0]
print(find_peak_of_mountain(arr))  