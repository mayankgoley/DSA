def next_greater_number(nums):
    n = len(nums)
    stack = []
    result = [-1] * n

    for i in range(2*n):
        curr = nums[i%n]
        while stack and nums[stack[-1]] < curr:
            index = stack.pop()
            result[index] = curr
        
        if i< n:
            stack.append(i)
    
    return result

# Example usage
nums = [1, 2, 1]
print(next_greater_number(nums))  # Output: [2, -1, 2]