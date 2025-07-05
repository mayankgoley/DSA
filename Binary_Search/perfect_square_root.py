def perfect_square_root(x):
    if x < 0:
        return False
    
    if x == 0 or x == 1:
        return True
    
    left, right = 0 , x -1
    
    while left <=right:
        mid = (left + right) // 2

        if mid * mid == x:
            return True
        elif mid * mid < x:
            left +=1
        else:
            right -=1
    
    return False

# Example usage:
x = 16
print(perfect_square_root(x))