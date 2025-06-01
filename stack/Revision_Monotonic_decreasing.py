#We are finding the next greater element in a monotonic decreasing stack.
# This means We pop while the current element is greater than the element at the top of the stack.
# This is useful in problems where we need to find the next greater element for each element in an array.
# This is a simple implementation of a monotonic decreasing stack.

def next_greater_element(arr):
    n = len(arr)
    result = [-1] * n
    stack = [] # We will use this stack to store indices of elements whose next greater elements we are trying to find
    for i in range(n):
        # While the stack is not empty AND the current element is greater than
        # the element at the top index of the stack (i.e., arr[stack[-1]]):
        # → This means we've found a "next greater element" for the index on top of the stack.
        while stack and arr[i] > arr[stack[-1]]:
            top_index = stack.pop()
            result[top_index] = arr[i]
        stack.append(i)
    return result

# Example usage
arr = [5, 10, 15, 20, 4, 20, 25]
print(next_greater_element(arr))
# Output: [10, 15, 20, -1, 20, 25, -1]
# This will print the next greater element for each element in the array.