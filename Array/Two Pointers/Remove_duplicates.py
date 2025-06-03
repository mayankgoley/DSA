# Remove duplicates from a sorted array in-place and return the new length.

def remove_duplicates(nums):
    left = 0
    for right in range(1, len(nums)):
        if nums[left] != nums[right]:
            left +=1
            nums[left] = nums[right]
    return left +1

# Example usage:
nums = [1, 1, 2, 2, 3, 4, 4]
new_length = remove_duplicates(nums)
print("New length:", new_length)