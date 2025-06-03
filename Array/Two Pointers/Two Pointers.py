def two_sum(nums, target):
    """
    Find two numbers in the list that add up to the target.
    """

    left = 0
    right = len(nums) - 1
    result = []

    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            result.append([nums[left], nums[right]])
            left +=1
            right -=1
        elif current_sum < target:
            left +=1
        else:
            right -=1
    return result if result else None
    # If no pairs found, return an empty list
    


# Example usage:
nums = [1, 2, 3, 4, 5]
target = 6
result = two_sum(nums, target)
print(result)