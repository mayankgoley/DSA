def two_pointers(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        second = target - num
        if second in seen:
            return [seen[second], i]
        seen[num] = i

nums = [2, 7, 11, 15]
target = 9

print(two_pointers(nums, target))