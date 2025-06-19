"""
Given an integer array nums, return all unique triplets [nums[i], nums[j], nums[k]] such that:

i != j != k
nums[i] + nums[j] + nums[k] == 0
You must return the list of triplets with no duplicates, and order doesn’t matter.
"""
def three_sum(nums):
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n -2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left, right = i+1, n-1

        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left +=1
            elif total > 0:
                right -=1
            else:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left +1]:
                    left +=1
                while left < right and nums[right] == nums[right -1]:
                    right -=1
                left +=1
                right -=1
    return result
# Example usage:
nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))  # Output: [[-1, -1, 2], [-1, 0, 1]]