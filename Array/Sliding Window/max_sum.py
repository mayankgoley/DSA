def max_sum(nums, k):
    n = len(nums)
    max_sum = current_sum = sum(nums[:k])

    for i in range(k, n):
        current_sum = current_sum - nums[i-k] + nums[i]
        max_sum = max(max_sum, current_sum)

    return max_sum

nums = [2, 1, 5, 1, 3, 2]
k = 3

print(max_sum(nums, k))