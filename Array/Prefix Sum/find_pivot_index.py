def pivot_index(arr):
    total = sum(arr)
    n = len(arr)
    left_sum = 0

    for i in range(len(arr)):
        if left_sum == (total - left_sum - arr[i]):
            return i
        left_sum = left_sum + arr[i]

    return -1

arr = [1, 7, 3, 6, 5, 6]

print(pivot_index(arr))