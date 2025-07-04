"""
For each element in array 1, find the next greater element in array 2.
If no greater element exists, return -1."""

def next_greater_element(nums1, nums2):
    stack = []
    next_greater = {}

    # Create a mapping of next greater elements for nums2
    for nums in nums2:
        while stack and stack[-1] < nums:
            next_greater[stack.pop()] = nums
        stack.append(nums)

    # For elements in nums1, find their next greater element in nums2
    result = []
    for num in nums1:
        result.append(next_greater.get(num, -1))
    return result

# Example usage
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(next_greater_element(nums1, nums2))