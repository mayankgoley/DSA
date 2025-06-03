"""
You're given an array height[], where each element represents the height of a vertical line drawn on the x-axis.
You must choose two lines that, along with the x-axis, form a container to hold water.

Your goal is to find the maximum area of water the container can store.
"""

def max_area(height):
    left = 0
    right = len(height) -1
    max_area = 0
    while left < right:
        width = right - left
        h = min(height[left], height[right])
        area = width * h
        max_area = max(max_area, area)
        if height[left] < height[right]:
            left +=1
        else:
            right -=1
    return max_area
# Example usage:
height = [1,8,6,2,5,4,8,3,7]
print(max_area(height))  