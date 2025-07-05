def sqrt(x):
    if x < 2 and x >= 0:
        return x
    
    left, right = 0, x

    while left <= right:
        mid = (left + right) // 2
        

        if mid * mid <= x:
            ans = mid
            left = mid +1
        else:
            right = mid - 1

    return ans

# Example usage:
x= 8
result = sqrt(x)
print(result)