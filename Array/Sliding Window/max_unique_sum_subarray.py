"""
You are given an integer array nums. You want to select a subarray with all unique elements, and your score is the sum of that subarray.

Return the maximum score you can get."""

def max_unique_sum_subarray(nums):
    n = len(nums)
    seen = set()
    left = 0
    curr_sum = 0
    max_sum = 0

    for right in range(0, len(nums)):
        while nums[right] in seen:
            seen.remove(nums[left])
            curr_sum -=nums[left]
            left +=1

        seen.add(nums[right])
        curr_sum += nums[right]
        max_sum = max(max_sum, curr_sum)

    return max_sum

nums = [4,2,4,5,6]
print(max_unique_sum_subarray(nums))