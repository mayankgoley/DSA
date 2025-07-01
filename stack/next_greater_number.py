def next_greater_number(nums1, nums2):
    stack = []
    next_greater = {}

    for num in nums2:
        while stack and stack[-1] < num:
            prev = stack.pop()
            next_greater[prev] = num
        stack.append(num)

    
    result = []
    for num in nums1:
        if num in next_greater:
            result.append(next_greater[num])
        else:
            result.append(-1)

    return result

# Example usage
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
print(next_greater_number(nums1, nums2))

