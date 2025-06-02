def next_greater_element(arr):
    n = len(arr)
    result = [-1] * n
    stack = []

    for i in range(n):
        while stack and arr[i] > arr[stack[-1]]:
            top_index = stack.pop()
            result[top_index] = arr[i]
        stack.append(i)
    return result

arr = [5, 10, 15, 20, 4, 20, 25]
print(next_greater_element(arr))