def next_maximum(temperatures):
    stack = []
    result = [0] * len(temperatures)

    for i, temp in enumerate(temperatures):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            index = stack.pop()
            result[index] = i - index
        stack.append(i)
    return result

# Example usage
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(next_maximum(temperatures))