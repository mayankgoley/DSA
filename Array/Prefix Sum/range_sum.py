'''
arr = [2, 4, 6, 8, 10]
Find the sum from index 1 to 3
output = 18
'''

def range_sum(arr,i,j):
    n = len(arr)
    prefix = [0] * n

    prefix[0] = arr[0]

    for k in range(1,n):
        prefix[k] = prefix[k-1] + arr[k]

    if i == 0:
        return prefix[j]
    
    else:
        return prefix[j] - prefix[i-1]
    
arr = [2, 4, 6, 8, 10]

print(range_sum(arr, 1, 3))