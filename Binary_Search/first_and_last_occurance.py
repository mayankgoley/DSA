def first_and_last_occurance(arr, target):
    def find_bound(arr, target, is_first):      
        left = 0
        right = len(arr) -1

        bound = -1

        while left <=right:
            mid = (left + right) // 2

            if arr[mid] == target:
                bound = mid
                if is_first:
                    right = mid -1
                else:
                    left = mid + 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid -1

        return bound
    
    return (find_bound(arr, target, True), find_bound(arr, target, False))

# Example usage:
arr = [1, 2, 2, 2, 2, 3, 4, 5]
target = 2
print(first_and_last_occurance(arr, target))  # Output: (1, 3)
