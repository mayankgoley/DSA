def max_avg_subarray(nums, k):
    n = len(nums)
    current_avg = sum(nums[:k])
    max_sum = current_avg

    for i in range(k, n):
        current_avg = current_avg - nums[i-k] + nums[i]
        max_sum = max(max_sum, current_avg)

    return max_sum/k

nums = [1,12,-5,-6,50,3]
k = 4

print(max_avg_subarray(nums, k))