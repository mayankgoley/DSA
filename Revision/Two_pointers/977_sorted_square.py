"""
Brute Force approach to sort the squares of a list of integers.
def sorted_squares(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] * nums[i]
    
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums
# Example usage:
nums = [-4, -1, 0, 3, 10]
print(sorted_squares(nums)) """

"""Two Pointers approach to sort the squares of a list of integers."""

def sorted_squares(nums):
    n = len(nums)
    result = [0] * n
    left, right = 0, n-1
    position = n - 1

    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result[position] = nums[left] * nums[left]
            left +=1
        else:
            result[position] = nums[right] * nums[right]
            right -=1
        position -=1
    
    return result

# Example usage:
nums = [-4, -1, 0, 3, 10]
print(sorted_squares(nums))
