def prefix_sum(arr):
    n = len(arr)

    pf = [0] * n
    pf[0] = arr[0]

    for i in range(1, n):
        pf[i] = pf[i-1] + arr[i]

    return pf

arr = [3,1,4,2,5]

print(prefix_sum(arr))