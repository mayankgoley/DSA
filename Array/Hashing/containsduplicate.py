def containsduplicate(nums):
    seen = {}

    for i , num in enumerate(nums):
        if num in seen:
            return True
        seen[num] = i
    return False

nums = [1, 2, 3, 1]
print(containsduplicate(nums))